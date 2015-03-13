#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05

import json

from django.db.models import Q

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from apps.db.models import News, Newswatch, MynewswatchList, NewsRemind
from apps.libs.views import get_default_list

@login_required(login_url='/login/')
def news(request, template):
    search = request.GET.get('search', '')
    user_id = request.user.id
    list_id = request.GET.get('list_id', '')
    if search:
        news_data = News.objects.filter(source__icontains=search)
    else:
        news_data = News.objects.all()
    news_source = []
    for i in news_data:
        news_source.append(i.source)
    if list_id:
        mod_list_data = MynewswatchList.objects.get(id=list_id)
    else:
        mod_list_data = MynewswatchList.objects.order_by('-id')[0]

    default_result = get_default_list(request)
    content = {
        'search': search,
        'mod_list_data': mod_list_data,
        'default_result': default_result,
        'news_source': set(news_source),
        'request': request
    }
    return TemplateResponse(request, template, content)

def set_news_watch(request):
    ''' 设置关注的新闻
    '''
    data = eval(request.GET.get('data', {}))
    source = data.get('source', '')
    entity = data.get('entity', '')
    incident = data.get('incident', '')
    user = request.user
    list_id = request.GET.get('list_id', '')
    watch_list_data = MynewswatchList.objects.get(id=list_id)
    for i in source:
        for j in entity:
            for k in incident:
                news_watch = Newswatch(
                        user=user,
                        watch_list_name=watch_list_data,
                        source=i,
                        entity=j,
                        incident=k
                    )
                news_watch.save()
    return HttpResponse(200)


def set_news_list(request):
    '''设置新的列表
    '''
    name = request.GET.get('name', '').strip()
    user = request.user
    if name:
    	mywatch = MynewswatchList(user=user, list_name=name)
    	mywatch.save()
    	list_data = MynewswatchList.objects.order_by('-id')[0]
    	return HttpResponse(json.dumps({'list_id': list_data.id, 'code': 200}))
    else:
        return HttpResponse(json.dumps({'code': 500, 'msg': u'不能设置空的列表！！'}))

def get_watch_list(request, news_list, watch_list):
    watchs = {}
    result = []
    watch_dict = {}
    for i in news_list:
        watchs[('%s-%s-%s')%(i.source, i.entity, i.incident)] = i.watch_list_name.list_name
    for i in watch_list:
        watch_dict[i.list_name] = {'list_id': i.id, 'news_list': []}
    for i in watchs:
        try:
            watch_dict[watchs[i]]['news_list'].append(i)
        except KeyError:
            pass
    for i in watch_dict:
        result.append({
            'name': i,
            'list_id': watch_dict[i]['list_id'],
            'news_list': watch_dict[i]['news_list']
        })
    return result

def modif_list(request):
    ''' 修改列表名称
    '''

    list_name = request.GET.get('list_name')
    list_id = request.GET.get('list_id')
    list_data = MynewswatchList.objects.get(id=list_id)
    list_data.list_name = list_name
    list_data.save()
    reverse_url = '/news/?list_id=%s' % list_id
    return HttpResponseRedirect(reverse_url)

def news_remind(request):
    ''' 获取新闻提醒
    '''

    source_list = []
    entity_list = []
    incident_list = []
    user = request.user
    remind_data = NewsRemind.objects.get(user=user)
    remind_news = Newswatch.objects.filter(user=user)
    last_search_time = remind_data.last_search_time
    for i in remind_news:
        source_list.append(i.source)
        entity_list.append(i.entity)
        incident_list.append(i.incident)
    source_list = list(set(source_list))
    entity_list = list(set(entity_list))
    incident_list = list(set(incident_list))
    news_data = News.objects.filter(Q(incident__in=incident_list),Q(source__in=source_list), Q(entity__in=entity_list), news_time__gt=last_search_time)
    result = json.dumps({'count': news_data.count()})
    return HttpResponse(result)
