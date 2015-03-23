#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05

import sys
import json
import datetime

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q

from apps.db.models import Instrument, News, Price, Listinter, Interlistwatch, WebSentimentHourly, FtrCustomerSentimentHourly, WebSiteitemsraw, WebFeedsites, FtrEventRaw
from apps.libs.views import get_default_list

reload(sys)
sys.setdefaultencoding('utf-8')

def get_exchange(request):
    exchange_list = []
    result = {}
    data = Instrument.objects.all()
    for i in data:
        exchange_list.append(i.exchange_id.exchange_name)
    for i in set(exchange_list):
        result[i] = {'id': '', 'instrument': []}
    for i in data:
        result[i.exchange_id.exchange_name]['instrument'].append({'id': i.id, 'name': i.instrument_name})
        result[i.exchange_id.exchange_name]['id'] = i.exchange_id.id
    return result

@login_required(login_url='/login/')
def stock(request, template):
    need_watch_instr = ''
    is_watched = True
    default_result = get_default_list(request)
    search_intr = request.GET.get('in_id', '')
    user_id = request.user.id
    if search_intr:
        need_watch_instr = Instrument.objects.get(id__exact=int(search_intr))
        watched_list = Interlistwatch.objects.filter(Q(user=user_id), Q(instr_name=need_watch_instr))
        if watched_list:
            is_watched = False
    content = {
        'is_watched': is_watched,
        'need_watch_instr': need_watch_instr,
        'default_result': default_result,
        'request': request,
    }
    return TemplateResponse(request, template, content)

@login_required(login_url='/login/')
def get_chart_data(request):
    ''' 获取曲线图数据
    '''

    date_list = []
    price_list = []
    sentiment_list = []
    result = {'instrument': '', 'time': [], 'price_value': [], 'instrument_fasi': []}
    search_id = 1
    instrId = request.GET.get('instrId', '')
    instr_name = request.GET.get('instr_name', '')
    if instrId:
        search_id = instrId
        data = WebSentimentHourly.objects.filter(instrument_id=search_id).order_by('date', 'hour')
        for i in data:
            result['time'].append('%s %s:00' % (i.date, i.hour))
            result['price_value'].append(i.price.replace(',', '').replace('$', ''))
            result['instrument_fasi'].append(str(i.sentiment))
    #if instr_name:
    #    data = Price.objects.filter(instrument_id__instrument_name=instr_name).order_by('date_time')

    result_json = json.dumps(result)
    return HttpResponse(result_json)

@login_required(login_url='/login/')
def set_instr_watch(request):
    ''' 设置关注股票
    '''
    result = {'status': 200}
    user = request.user
    watch_id = request.GET.get('instrId')
    instrument_data = Instrument.objects.filter(id=watch_id)
    obj = InstrWatch(user=user, instrument=instrument_data[0])
    obj.save()
    result_json = json.dumps(result)
    return HttpResponse(result_json)

@login_required(login_url='/login/')
def add_to_list(request):
    ''' 添加股票至列表
    '''
    list_id = request.GET.get('to_list', '')
    instr_id = request.GET.get('instr_id', '')
    instr_name = request.GET.get('instr_name', '')
    list_obj = Listinter.objects.get(id=list_id)
    if instr_name:
        instr_obj = Instrument.objects.get(short_name=instr_name)
    elif instr_id:
        instr_obj = Instrument.objects.get(id=instr_id)
    db_data = Interlistwatch.objects.filter(user = request.user, list_name = list_obj, instr_name = instr_obj.short_name)
    if db_data:
        return HttpResponse(json.dumps({'code': 500, 'msg': u'该股票已存在此列表中！！'}))
    else:
        instr_list = Interlistwatch(
                user = request.user,
                list_name = list_obj,
                instr_name = instr_obj.short_name,
                instr_id = instr_obj.id
            )
        instr_list.save()
    if instr_name:
        return HttpResponse(json.dumps({'code': 200, 'instr_id': instr_obj.id}))
    elif instr_id:
        reverse_url = '/stock?in_id=%s'%instr_id
        return HttpResponseRedirect(reverse_url)

@login_required(login_url='/login/')
def get_news(request):
    result = {
        'id': '',
        'title': '',
        'content': [],
        'link': '',
        'fasi': '',
        'time': '',
        'source': '',
        'instrument': {'id': '', 'name': ''},
        'industry': {'id': '', 'name': ''}
    }
    result_list = []
    instr_id = request.GET.get('instrId', '')
    date_time = request.GET.get('time', '')
    if instr_id:
        news_data = FtrCustomerSentimentHourly.objects.filter(instrument_id=instr_id)
    else:
        i_id = request.GET.get('instr_id', '')
        times = date_time.split(' ')
        day = times[0]
        hour = times[1][:-3]
        news_data = FtrCustomerSentimentHourly.objects.filter(instrument_id=i_id, date=day, hour=hour)
        #news_data = News.objects.filter(news_time__contains=date_time)
    raw_list = []

    for i in news_data:
        raw_list.append(i.siteitemsraw_id)
    news_data = WebSiteitemsraw.objects.filter(id__in=list(set(raw_list))).order_by('-item_date')[:20]
    for i in news_data:
        site_name = WebFeedsites.objects.get(id=i.site_id)
        result_list.append({
            'id': i.id,
            'title': i.item_title,
            'time': i.item_date.strftime("%Y-%m-%d %H:%M:%S"),
            'link': i.item_url,
            'source': site_name.site_name,
            'content': [],

        })
    for i in result_list:
        event_id_list = []
        events_detail = FtrEventRaw.objects.filter(news_id=i['id'])
        for e in events_detail:
            i['content'].append(e.event_phrase)
    #    result_list.append({
    #        'id': i.id,
    #        'title': i.news_title,
    #        'content': i.news_content,
    #        'link': i.news_link,
    #        'fasi': i.news_fasi,
    #        'time': i.news_time.strftime("%Y-%m-%d %H:%M:%S"),
    #        'source': i.source,
    #        'instrument': {
    #            'id': i.instrument_id.id,
    #            'name': i.instrument_id.instrument_name
    #        },
    #        'industry': {
    #            'id': i.industry_classification.id,
    #            'name': i.industry_classification.industry_classification_name
    #        }
    #        })
    result = json.dumps(result_list)
    return HttpResponse(result)

@login_required(login_url='/login/')
def add_watch_list(request):
    result = {
        'code': '',
        'msg': ''
    }
    user = request.user
    new_watch_name = request.GET.get('watched_name', '').strip()
    if new_watch_name:
        watched_list = Listinter(
            user = user,
            name = new_watch_name
        )
        watched_list.save()
        result['code'] = 200
    else:
        result['code'] = 500
        result['msg'] = u'列表名称不能为空！！'
    return HttpResponse(json.dumps(result))

def remove_watch(request):
    instr_name = request.GET.get('instrname', '').strip()
    user = request.user
    instr_obj = Instrument.objects.filter(instrument_name=instr_name)
    instr_data = Interlistwatch.objects.get(inter_list=instr_obj[0], user=user)
    instr_data.delete()
    now_path = request.get_full_path()
    return HttpResponse(json.dumps({'code': 200}))
