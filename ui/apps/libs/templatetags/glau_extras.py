#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from apps.db.models import Country

register = template.Library()

@register.filter()
def is_atten(data, instr):
    atten_list = []
    for i in data:
        atten_list.append(i.instrument.id)
    return (instr in atten_list)

@register.filter()
def get_country(code):
    name = Country.objects.filter(country_iso_code=code)
    country_name = name[0]
    return country_name
