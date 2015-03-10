#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nataila @ 2015-01-07

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class UserAddForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件：')

    #def clean_email(self):
    #    email = self.cleaned_data['email']
    #    if not email:
    #        raise forms.ValidationError('can not empty')


    def save(self):
        user = User.objects.create_user(
            self.cleaned_data['username'].strip().lower(),
            self.cleaned_data['email'].strip(),
            self.cleaned_data['password'].strip()
        )
        user.save()

        return user

class UserPasswordForm(PasswordChangeForm):
    '''用户修改自己个人密码表单'''

    old_password = forms.CharField(label=(u'旧密码: (*)'),
        widget=forms.PasswordInput(attrs={'class': 'text'}))
    new_password1 = forms.CharField(label=(u'新密码: (*)'),
        widget=forms.PasswordInput(attrs={'class': 'text'}),
    )
    new_password2 = forms.CharField(label=u'确认密码: (*)',
        widget=forms.PasswordInput(attrs={'class': 'text'}))

    def clean_new_password1(self):
        """检查新密码

        """

        new_password1 = self.cleaned_data['new_password1']
        new_password2 = self.cleaned_data['new_password2']
        return new_password1
