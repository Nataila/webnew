#!/usr/bin/env python
# coding: utf-8

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Issuer(models.Model):
    """ 发行者
    """

    id = models.IntegerField(primary_key=True)
    short_name = models.CharField(max_length=100, blank=True)
    long_name = models.CharField(max_length=100, blank=True)
    register_city = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'issuer'

    def __unicode__(self):
        return u'%s' % (self.long_name)

class IssuerAdmin(admin.ModelAdmin):
    list_dispaly = ('long_name',)

class Country(models.Model):
    """ 国家
    """

    country_iso_code = models.CharField(primary_key=True, max_length=50)
    country_name = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = 'country'

    def __unicode__(self):
        return u'%s' % (self.country_name)
class CountryAdmin(admin.ModelAdmin):
    list_dispaly = ('country_name',)



class Exchange(models.Model):
    """ 交易所
    """

    id = models.IntegerField(primary_key=True)
    short_name = models.CharField(max_length=50, blank=True)
    long_name = models.CharField(max_length=50, blank=True)
    country_iso_code = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return u'%s' % (self.long_name)
class ExchangeAdmin(admin.ModelAdmin):
    list_dispaly = ('long_name',)


class IndustryClassification(models.Model):
    """ 行业
    """
    id = models.IntegerField(primary_key=True)
    classification_standard = models.CharField(max_length=50, blank=True)
    classification_name = models.CharField(max_length=80, blank=True)
    parent_classification = models.ForeignKey('self', blank=True, null=True)
    class Meta:
        db_table = 'industry_classification'


    def __unicode__(self):
        return u'%s' % (self.classification_name)

class IndustryClassificationAdmin(admin.ModelAdmin):
    list_dispaly = ('classification_name',)


class Instrument(models.Model):
    """ 证券
    """

    id = models.IntegerField(primary_key=True)
    short_name = models.CharField(max_length=50, blank=True)
    long_name = models.CharField(max_length=100, blank=True)
    instrument_type = models.CharField(max_length=50, blank=True)
    issuer = models.ForeignKey('Issuer', blank=True, null=True)
    exchange = models.ForeignKey(Exchange, blank=True, null=True)
    industry_classification = models.ForeignKey(IndustryClassification, blank=True, null=True)
    class Meta:
        db_table = 'instrument'

    def __unicode__(self):
        return u'%s' % (self.short_name)
class InstrumentAdmin(admin.ModelAdmin):
    list_dispaly = ('short_name',)

class Identifier(models.Model):
    """ 识别符
    """
    id = models.IntegerField(primary_key=True)
    instrument_id = models.IntegerField(blank=True, null=True)
    identifier_type = models.CharField(max_length=10, blank=True)
    identifier_value = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=50, blank=True)
    currency_code = models.CharField(max_length=10, blank=True)
    exchange = models.ForeignKey(Exchange, blank=True, null=True)
    class Meta:
        db_table = 'identifier'

    def __unicode__(self):
        return u'%s' % (self.identifier_value)

class IdentifierAdmin(admin.ModelAdmin):
    list_dispaly = ('identifier_value',)


class Price(models.Model):
    """ 价格
    """

    instrument_id = models.CharField(max_length=16, blank=True)
    date_time = models.DateTimeField(blank=True, null=True)
    open = models.TextField(blank=True) # This field type is a guess.
    high = models.TextField(blank=True) # This field type is a guess.
    low = models.TextField(blank=True) # This field type is a guess.
    close = models.TextField(blank=True) # This field type is a guess.
    volume = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    class Meta:
        db_table = 'price'

    def __unicode__(self):
        return u'%s' % (self.instrument_id)

class PriceAdmin(admin.ModelAdmin):
    list_dispaly = ('ticker')

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

    id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    watchlist_name = models.CharField(max_length=50, blank=True)
    instrument = models.ForeignKey(Instrument, blank=True, null=True)

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
    industry_classification = models.ForeignKey(IndustryClassification, verbose_name=u'所属板块')


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
    #inter_list = models.ForeignKey(Instrument, verbose_name=u'股票', null=True, blank=True)
    instr_name = models.CharField(max_length=100, verbose_name=u'关注的股票名称', null=True, blank=True)
    instr_id = models.CharField(max_length=20, verbose_name=u'股票id', null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.list_name)

class InterlistwatchAdmin(admin.ModelAdmin):
    list_dispaly = ('list_name', 'inster_list')

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


class WebSentimentHourly(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    hour = models.SmallIntegerField()
    instrument_id = models.CharField(max_length=16)
    sentiment = models.DecimalField(max_digits=25, decimal_places=2, blank=True, null=True)
    price = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'web_sentiment_hourly'

class FtrCustomerSentimentHourly(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    hour = models.SmallIntegerField(blank=True, null=True)
    instrument_id = models.CharField(max_length=6, blank=True)
    siteitemsraw_id = models.IntegerField(blank=True, null=True)
    customer_sentiment_raw_id = models.IntegerField(blank=True, null=True)
    polarity = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ftr_customer_sentiment_hourly'

class WebFeedsites(models.Model):
    id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=30)
    site_url = models.CharField(max_length=200)
    site_desc = models.TextField(blank=True)
    site_created_date = models.DateTimeField()
    site_parser = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'web_feedsites'

class WebSiteitemsraw(models.Model):
    id = models.IntegerField(primary_key=True)
    site = models.ForeignKey(WebFeedsites)
    item_title = models.TextField()
    item_subtitle = models.TextField(blank=True)
    item_url = models.CharField(max_length=200)
    item_created_date = models.DateTimeField()
    item_collector_version = models.IntegerField()
    item_date = models.DateTimeField()
    item_raw = models.TextField()
    class Meta:
        managed = False
        db_table = 'web_siteitemsraw'

class FtrEventRaw(models.Model):
    id = models.IntegerField(primary_key=True)
    news_id = models.IntegerField(blank=True, null=True)
    event_scope = models.CharField(max_length=100, blank=True)
    event_type = models.CharField(max_length=100, blank=True)
    direction = models.CharField(max_length=100, blank=True)
    expectation = models.CharField(max_length=100, blank=True)
    expectation_bias = models.CharField(max_length=100, blank=True)
    sentiment = models.CharField(max_length=100, blank=True)
    event_phrase = models.TextField(blank=True)
    quote_organization = models.CharField(max_length=100, blank=True)
    quote_person = models.CharField(max_length=100, blank=True)
    nlp_history_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ftr_event_raw'
