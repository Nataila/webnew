#!/usr/bin/env python
# coding=utf-8


"""
用户管理模型
============

* 用户信息表
"""


from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """用户Profile表"""

    user = models.OneToOneField(User, unique=True)

    realname = models.CharField(max_length=150)
    mobile = models.CharField(max_length=11, null=True)
    tel = models.CharField(max_length=13, null=True)
    fax = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)  # 为了支持多E-mail的情况而设定 用英文逗号","分隔
    department = models.CharField(null=True, max_length=30, default='')  # 所属部门

    class Meta:
        db_table = 'user_profile'
