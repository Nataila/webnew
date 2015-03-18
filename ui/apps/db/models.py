#!/usr/bin/env python
# coding: utf-8

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Issuser(models.Model):
    """ 发行者
    """

    issuer_name = models.CharField(max_length=120, verbose_name = u'发行者名称')
    #class Meta:
    #    db_table = 'issuer'

    def __unicode__(self):
        return u'%s' % (self.issuer_name)
class IssuerAdmin(admin.ModelAdmin):
    list_dispaly = ('issuer_name',)


class Exchange(models.Model):
    """ 交易所
    """

    short_name = models.CharField(max_length=120, verbose_name = u'交易所简称')
    long_name = models.CharField(max_length=120, verbose_name = u'交易所全称')
    country_iso_code = models.CharField(max_length=120, verbose_name = u'国家')
    #country_iso_code = models.ForeignKey(Country, verbose_name = u'国家')
    #class Meta:
    #    db_table = 'exchange'

    def __unicode__(self):
        return u'%s' % (self.exchange_name)
class ExchangeAdmin(admin.ModelAdmin):
    list_dispaly = ('exchange_name',)


class Industry_classification(models.Model):
    """ 行业
    """

    industry_classification_name = models.CharField(max_length=120, verbose_name = u'行业名称')
    parent_classification_id = models.CharField(max_length=120, verbose_name = u'行业上级分类代码')
    parent_classification_name = models.CharField(max_length=120, verbose_name = u'行业上级分类名称')
    classification_set = models.CharField(max_length=120, verbose_name = u'分类标准')
    exchange_id = models.ForeignKey(Exchange, verbose_name = u'所属证交所')
    #class Meta:
    #    db_table = 'IndustryClassification'

    def __unicode__(self):
        return u'%s' % (self.industry_classification_name)
class Industry_classificationAdmin(admin.ModelAdmin):
    list_dispaly = ('industry_classification_name',)


class Instrument(models.Model):
    """ 证券
    """

    instrument_id = models.IntegerField(verbose_name = u'证券代码', unique=True)
    instrument_name = models.CharField(max_length=120, verbose_name = u'证券名称')
    instrument_type = models.CharField(max_length=80, verbose_name = u'证券类型')
    issuer_id = models.ForeignKey(Issuser, verbose_name = u'发行者')
    exchange_id = models.ForeignKey(Exchange, verbose_name = u'交易所')
    industry_classification_id = models.ForeignKey(Industry_classification, verbose_name = u'版块')
    #class Meta:
    #    db_table = 'instrument'

    def __unicode__(self):
        return u'%s' % (self.instrument_name)
class InstrumentAdmin(admin.ModelAdmin):
    list_dispaly = ('instrument_name',)


class Country(models.Model):
    """ 国家
    """

    country_name = models.CharField(max_length=120, verbose_name = u'国家名称')
    country_iso_code = models.CharField(max_length=120, verbose_name = u'国家')
    #class Meta:
    #    db_table = 'country'

    def __unicode__(self):
        return u'%s' % (self.country_name)
class CountryAdmin(admin.ModelAdmin):
    list_dispaly = ('country_name',)


class Identifier(models.Model):
    """ 识别符
    """
    instrument_id = models.ForeignKey(Instrument)
    identifier_type = models.CharField(max_length=120, verbose_name = u'识别符类别')
    identifier_value = models.CharField(max_length=120, verbose_name = u'识别符值')
    #class Meta:
    #    db_table = 'identifier'

    def __unicode__(self):
        return u'%s' % (self.identifier_type)
class IdentifierAdmin(admin.ModelAdmin):
    list_dispaly = ('identifier_value',)


class Price(models.Model):
    """ 价格
    """

    instrument_id = models.ForeignKey(Instrument)
    date_time = models.DateTimeField(auto_now_add=False, verbose_name=u'日期时间')
    #price_type = models.CharField(max_length=120, verbose_name = u'价格类型')
    close = models.CharField(max_length=120, verbose_name = u'价格值')
    #instrument_fasi = models.CharField(max_length=120, verbose_name = u'情绪值')
    #class Meta:
    #    db_table = 'price'

    def __unicode__(self):
        return u'%s' % (self.instrument_id)
class PriceAdmin(admin.ModelAdmin):
    list_dispaly = ('price_value', 'instrument_fasi', 'date_time')


class Fasi(models.Model):
    """情绪值
    """
    instrument_id = models.ForeignKey(Instrument)
    date_time = models.DateTimeField(auto_now_add=False, verbose_name=u'日期时间')
    date = models.DateTimeField(auto_now_add=False, verbose_name=u'日期')
    hour = models.IntegerField(verbose_name = u'小时', unique=True)
    #class Meta:
    #    db_table = 'fasi'
    def __unicode__(self):
        return u'%s' % (self.instrument_id)

class FasiAdmin(admin.ModelAdmin):
    list_dispaly = ('date',)


class Customer(models.Model):
    """ 客户
    """
    customer_name = models.CharField(max_length=120, verbose_name = u'客户')

    def __unicode__(self):
        return u'%s' % (self.customer_name)
class CustomerAdmin(admin.ModelAdmin):
    list_dispaly = ('customer_name',)

class Watchlist(models.Model):
    """ 观察者
    """

    customer_id = models.ForeignKey(Customer)
    watchlist_name = models.CharField(max_length=120, verbose_name = u'观察者名单')
    instrument_id = models.ForeignKey(Instrument)

    def __unicode__(self):
        return u'%s' % (self.watchlist_name)
class WatchlistAdmin(admin.ModelAdmin):
    list_dispaly = ('watchlist_name',)

class News(models.Model):
    """ 新闻
    """
    INCIDENT_CHOICE = (
        (u'公告', u'公告'),
        (u'研报', u'研报'),
        (u'新闻', u'新闻')
    )

    ENTITY_CHOICE = (
        (u'中国', u'中国'),
        (u'美国', u'美国'),
        (u'其他', u'其他'),
    )
    news_title = models.CharField(max_length=120, verbose_name = u'新闻标题')
    news_content = models.TextField(verbose_name = u'内容')
    news_fasi = models.IntegerField(verbose_name = u'情绪指数')
    news_link =  models.CharField(max_length=120, verbose_name = u'原文链接')
    news_time = models.DateTimeField(auto_now_add=False, verbose_name=u'日期时间')
    source =  models.CharField(max_length=120, verbose_name = u'新闻来源')
    instrument_id = models.ForeignKey(Instrument, verbose_name=u'股票')
    incident = models.CharField(max_length=20, choices=INCIDENT_CHOICE, verbose_name=u'事件')
    entity = models.CharField(max_length=20, choices=ENTITY_CHOICE, verbose_name=u'主体')
    industry_classification = models.ForeignKey(Industry_classification, verbose_name=u'所属板块')


    def __unicode__(self):
        return u'%s' % (self.news_title)
class Listinter(models.Model):
    """ 关注的股票列表
    """

    user = models.ForeignKey(User, verbose_name=u'用户')
    name = models.CharField(max_length=120, verbose_name=u'列表名称')
    def __unicode__(self):
        return u'%s' % (self.name)
class ListinterAdmin(admin.ModelAdmin):
    list_dispaly = ('name',)

class NewsAdmin(admin.ModelAdmin):
    list_dispaly = ('news_title', 'news_link', 'news_time', 'news_fasi')

class Interlistwatch(models.Model):
    """ 关注的股票
    """

    user = models.ForeignKey(User)
    list_name = models.ForeignKey(Listinter)
    inter_list = models.ForeignKey(Instrument, verbose_name=u'股票', null=True)

    def __unicode__(self):
        return u'%s' % (self.list_name)

class InterlistwatchAdmin(admin.ModelAdmin):
    list_dispaly = ('list_name', 'for_user')

#class InstrWatch(models.Model):
#    """ 关注的股票
#    """
#    user = models.ForeignKey(User)
#    instrument = models.ForeignKey(Instrument, null=True)
#
#    def __unicode__(self):
#        return u'%s' % (self.user)
#class InstrWatchAdmin(admin.ModelAdmin):
#    list_dispaly = ('user', 'news', 'instrument')

class MynewswatchList(models.Model):
    user = models.ForeignKey(User)
    list_name = models.CharField(max_length=120, verbose_name=u'列表名称')

    def __unicode__(self):
        return u'%s' % (self.list_name)

class MynewswatchListAdmin(admin.ModelAdmin):
    list_dispaly = ('list_name',)

class Newswatch(models.Model):
    user = models.ForeignKey(User)
    watch_list_name = models.ForeignKey(MynewswatchList)
    source = models.CharField(max_length=120, verbose_name=u'新闻源')
    entity = models.CharField(max_length=120, verbose_name=u'实体')
    incident = models.CharField(max_length=120, verbose_name=u'事件')

    def __unicode__(self):
        return u'%s' % (self.source)
class NewswatchAdmin(admin.ModelAdmin):
    list_dispaly = ('source', 'entity', 'incident')


class NewsRemind(models.Model):
    user = models.ForeignKey(User)
    last_search_time = models.DateTimeField(auto_now_add=False, verbose_name=u'最后查询时间')

    def __unicode__(self):
        return u'%s' % (self.last_search_time)

class NewsRemindAdmin(admin.ModelAdmin):
    list_dispaly = ('user', 'last_search_time',)
