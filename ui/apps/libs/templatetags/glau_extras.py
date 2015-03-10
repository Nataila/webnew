#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.filter()
def is_atten(data, instr):
    atten_list = []
    for i in data:
        atten_list.append(i.instrument.id)
    return (instr in atten_list)

