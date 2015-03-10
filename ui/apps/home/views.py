#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-05

from django.db.models import Q
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

from apps.db.models import Instrument
from apps.libs.views import get_default_list

@login_required(login_url='/login/')
def index(request, template):
    user_id = request.user.id
    search = request.GET.get('search', '')
    instr_data = []
    if search:
        #instr_data = Instrument.objects.filter(Q(instrument_id__exact=search) | Q(instrument_name__exact=search))
        try:
            search = int(search)
            instr_data = Instrument.objects.filter(instrument_id__exact=search)
        except ValueError:
            instr_data = Instrument.objects.filter(instrument_name__contains=search)
    default_result = get_default_list(request) 
    content = {
        'search': search,
        'instr_data': instr_data,
        'request': request,
        'default_result': default_result
    }
    return TemplateResponse(request, template, content)
