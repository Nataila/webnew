#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05


from django.conf.urls import url, patterns

urlpatterns = patterns('apps.stock.views',
    url('^$', 'stock', {'template': 'stock/stock.html'}, 'stock'),
    url('^get_exchange/$', 'get_exchange'),
    url('^get_chart_data/$', 'get_chart_data'),
    url('^set_instr_watch/$', 'set_instr_watch'),
    url('^add_to_list/$', 'add_to_list', name='add_to_list'),
    url('^get_news/$', 'get_news'),
    url('^add_watch_list/$', 'add_watch_list', name='add_watch_list'),
    url('^remove_watch/$', 'remove_watch'),
)
