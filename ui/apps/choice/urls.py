#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-06


from django.conf.urls import url, patterns

urlpatterns = patterns('apps.choice.views',
    url('^$', 'choice', {'template': 'choice/choice.html'}, 'choice'),
    url('^get_choice_list$', 'get_choice_list'),
    url('^change_hot_chart$', 'change_hot_chart'),
    url('^hot_to_chart$', 'hot_to_chart'),
    url('^code_to_name$', 'code_to_name')
)
