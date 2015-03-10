#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05

from django.shortcuts import render
from apps.db.models import Instrument, News, Instrument, Price, Listinter, Interlistwatch, Newswatch, MynewswatchList

def get_default_list(request):
    default_result = {
        'my_watch_list': [],
        'watch_news': []
    }
    default_result['my_watch_list'] = get_my_watch_list(request)
    default_result['watch_news'] = get_watch_news_list(request)
    return default_result


def get_my_watch_list(request):
    watch_list = {}
    list_result = []
    mid_dict = {}
    user = request.user.id
    list_data = Interlistwatch.objects.filter(user=user)
    user_watched = Listinter.objects.filter(user=request.user)
    for i in user_watched:
        watch_list[i.name] = []
    for i in list_data:
        watch_list[i.list_name.name].append({'name': i.inter_list.instrument_name, 'id': i.inter_list.id})
    for i in user_watched:
        mid_dict[i.name] = i.id
    for i in watch_list:
        list_result.append({'list_name': i, 'data': watch_list[i]})
    for i in list_result:
        try:
            i['id'] = mid_dict[i['list_name']]
        except KeyError:
            i['id'] = []
    return list_result

def get_watch_news_list(request):
    watchs = {}
    result = []
    watch_dict = {}
    user_id = request.user.id
    news_list = Newswatch.objects.filter(user=user_id)
    watch_list = MynewswatchList.objects.filter(user=user_id)
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
