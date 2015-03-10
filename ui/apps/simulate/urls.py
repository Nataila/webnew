#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-13

from django.conf.urls import url, patterns

urlpatterns = patterns('apps.simulate.views',
    url('^$', 'simulate', {'template': 'simulate/simulate.html'}, 'simulate'),
    url('^get_result$', 'get_result')
)
