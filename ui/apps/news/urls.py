#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-08

from django.conf.urls import url, patterns

urlpatterns = patterns('apps.news.views',
    url('^$', 'news', {'template': 'news/news.html'}, 'news'),
    url('set_news_watch/$', 'set_news_watch'),
    url('set_news_list/$', 'set_news_list'),
    url('modif_list/$', 'modif_list', name='modif_list'),
    url('news_remind/$', 'news_remind', name='news_remind')
)
