#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05

import os
import json
import datetime

from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from apps.db.models import Instrument, Exchange, Country, IndustryClassification, Price
from apps.libs.views import get_default_list

@login_required(login_url='/login/')
def choice(request, template):
    result = {}
    exchange_to_country = {}
    mid = {}
    final_result = []
    industry_exchange = []
    instr_data = Instrument.objects.all()
    exchange_data = Exchange.objects.all()
    country_data = Country.objects.all()
    industry_data = IndustryClassification.objects.all()
    for i in country_data:
        exchange_to_country[i.country_name] = []
    for i in exchange_data:
        result[i.exchange_name] = []
    for i in instr_data:
        mid[i.exchange_id.country_iso_code.country_name] = []
    for i in instr_data:
        exchange_to_country[i.exchange_id.country_iso_code.country_name].append(i.exchange_id.exchange_name)
        result[i.exchange_id.exchange_name].append(i.instrument_name)
    for i in exchange_to_country:
        exchange_to_country[i] = set(exchange_to_country[i])
    for i in exchange_to_country:
        for j in exchange_to_country[i]:
            if result.get(j, []):
                instr = result[j]
            else:
                instr = []
            mid[i].append({'exchange_name': j, 'instrument': instr})
    for i in mid:
        final_result.append({'country': i, 'data': mid[i]})

    default_result = get_default_list(request)
    content = {
        'default_result': default_result,
        'request': request,
        'final_result': final_result
    }

    return TemplateResponse(request, template, content)


def get_choice_list(request):

    result = {
            'country_to_exchange': {},
            'exchange_to_industry': {},
            'industry_to_instr': {}
    }

    industry_to_instr = []
    exchange_to_industry = []
    country_to_exchange = []

    instr_data = Instrument.objects.all()
    exchange_data = Exchange.objects.all()
    country_data = Country.objects.all()
    industry_data = IndustryClassification.objects.all()

    for i in instr_data:
        industry_to_instr.append({i.industry_classification_id.industry_classification_name: i.instrument_name})
    for i in industry_data:
        result['industry_to_instr'][i.industry_classification_name] = []
    for i in industry_to_instr:
        result['industry_to_instr'][i.keys()[0]].append(i.values()[0])

    for i in industry_data:
        exchange_to_industry.append({i.exchange_id.exchange_name: i.industry_classification_name})
    for i in exchange_data:
        result['exchange_to_industry'][i.exchange_name] = []
    for i in exchange_to_industry:
        result['exchange_to_industry'][i.keys()[0]].append(i.values()[0])

    for i in exchange_data:
        country_to_exchange.append({i.country_iso_code.country_name: i.exchange_name})
    for i in country_data:
        result['country_to_exchange'][i.country_name] = []
    for i in country_to_exchange:
        result['country_to_exchange'][i.keys()[0]].append(i.values()[0])

    return HttpResponse(json.dumps(result))

def change_hot_chart(request):
    ''' 热图数据
    '''

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    name = request.GET.get('name', '')
    json_result = {
            'name': 'flare',
            'children': []
            }
    #json_file = os.path.join('/home/ubuntu/project/glaucusis/newsfeedsite/webnew/ui/static/choice', 'flare.json')
    json_file = os.path.join('/var/data/users/chenc3/opt/webnew/ui/apps/choice/static/choice', 'flare.json')
    industry_dict = {}
    exchange_data = Exchange.objects.get(exchange_name=name)
    industry_data = IndustryClassification.objects.filter(exchange_id=exchange_data)
    instr_data = Instrument.objects.filter(exchange_id=exchange_data)
    price_data = Price.objects.filter(instrument_id__in=instr_data, date_time__contains=today)

    for i in industry_data:
        industry_dict[i.industry_classification_name] = []
    for i in price_data:
        industry_dict[i.instrument_id.industry_classification_id.industry_classification_name].append({'name': i.instrument_id.instrument_name, 'size': i.instrument_fasi})
    for i in industry_dict:
        json_result['children'].append({'name': i, 'children': industry_dict[i]})


    json.dump(json_result, open(json_file, 'w'), indent=4)

    return HttpResponse(json.dumps({'code': 200}))

def hot_to_chart(request):
    ''' 热图跳转
    '''
    instr_name = request.GET.get('name', '')
    data = Instrument.objects.get(instrument_name=instr_name)
    return HttpResponse(json.dumps({'id': data.id}))

def code_to_name(request):
    '''通过id获取名字'''

    result = {}
    code = int(request.GET.get('code', ''))
    if code:
        data = Instrument.objects.filter(instrument_id=code)
        for i in data:
            result['name'] = i.instrument_name
    return HttpResponse(result['name'])
