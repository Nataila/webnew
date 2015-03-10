#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-04

from datetime import datetime

from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.template.response import TemplateResponse
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.forms import AuthenticationForm

from apps.users.forms import UserAddForm
from apps.libs.views import get_default_list
from apps.db.models import News, NewsRemind
from apps.users.forms import UserPasswordForm

def auth_login(request, template):
    """ 用户登录
    """

    form = AuthenticationForm()
    content = {
        'error_msg': '',
        'request': request,
        'form': form
    }
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                redirect_to = request.GET.get('next', settings.LOGIN_REDIRECT_URL)
                return HttpResponseRedirect(redirect_to)
            else:
                content['error_msg'] = u'验证失败！！'
                return TemplateResponse(request, template, content)
        else:
            content['error_msg'] = u'用户名或密码不正确！！'
            return TemplateResponse(request, template, content)

    return TemplateResponse(request, template, {'request': request, 'form': form})

def auth_logout(request):
    """ 用户退出
    """

    return logout_then_login(request, login_url=settings.LOGOUT_URL)

def register(request, template):
    """用户注册
    """
    form = UserAddForm()
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            now = datetime.now()
            user = User.objects.get(username=request.POST.get('username'))
            user_mind = NewsRemind()
            user_mind.user = user
            user_mind.last_search_time = now
            user_mind.save()
            return HttpResponseRedirect(reverse('pre_login'))

    return TemplateResponse(request, template, {'form': form})


def set_account(request, template):
    '''  写入最后查看提醒时间
    '''

    default_result = get_default_list(request)
    content = {
        'default_result': default_result,
        'request': request,
        'news_data': []
    }
    if request.method == 'GET':
        count = request.GET.get('news', '')
        if count:
            user = request.user
            now = datetime.now()
            news_remind = NewsRemind.objects.get(user=user)
            news_remind.last_search_time = now
            news_remind.save()
            news_data = News.objects.order_by('-news_time')[:int(count)]
            content['news_data'] = news_data
    return TemplateResponse(request, template, content)

def acount_password(request, template):
    username = request.user.username
    content = {
        'request': request,
        'message': ''
    }

    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        user = authenticate(username=username, password=old_password)
        print user
        if user is not None:
            if new_password1 == new_password2:
                content['message'] = u'重置密码成功!!'
                user.set_password(new_password1)
                user.save()
            else:
                content['message'] = u'两次密码输入不一致!!'
        else:
            content['message'] = u'原密码不正确!!'
        return TemplateResponse(request, template, content)
