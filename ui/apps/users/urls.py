#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05

from django.conf.urls import url, patterns
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='sho/NewHome.html'), name='newhomw'),
    url(r'product/$', TemplateView.as_view(template_name='sho/product.html'), name='product'),
    url(r'trial/$', TemplateView.as_view(template_name='sho/trial.html'), name='trial'),
    url(r'inst/$', TemplateView.as_view(template_name='sho/inst.html'), name='inst'),
    url(r'^pre_login$', 'apps.users.views.auth_login', {'template': 'sho/login2.html'}, 'pre_login'),
)
