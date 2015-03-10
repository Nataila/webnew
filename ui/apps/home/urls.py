#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05

from django.conf.urls import url, patterns

urlpatterns = patterns('apps.home.views',
    url('^$', 'index', {'template': 'home/home.html'}, 'index')
)
