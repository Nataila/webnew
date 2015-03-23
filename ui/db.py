# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class CeleryTaskmeta(models.Model):
    id = models.IntegerField(primary_key=True)
    task_id = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    result = models.TextField(blank=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True)
    hidden = models.BooleanField()
    meta = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'celery_taskmeta'

class CeleryTasksetmeta(models.Model):
    id = models.IntegerField(primary_key=True)
    taskset_id = models.CharField(max_length=255)
    result = models.TextField()
    date_done = models.DateTimeField()
    hidden = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'celery_tasksetmeta'

class Country(models.Model):
    country_iso_code = models.CharField(max_length=50)
    country_name = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'country'

class CustomerPolarity(models.Model):
    id = models.IntegerField()
    customer_id = models.IntegerField(blank=True, null=True)
    scope_id = models.IntegerField(blank=True, null=True)
    event_type_id = models.IntegerField(blank=True, null=True)
    event_subtype_id = models.IntegerField(blank=True, null=True)
    polarity = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'customer_polarity'

class CustomerScope(models.Model):
    customer_scope_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    scope_id = models.IntegerField()
    event_type_id = models.IntegerField()
    event_type_scope_class_id = models.IntegerField(blank=True, null=True)
    event_type_scope_instance_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'customer_scope'

class DbCustomer(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=120)
    class Meta:
        managed = False
        db_table = 'db_customer'

class DbExchange(models.Model):
    id = models.IntegerField(primary_key=True)
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=50)
    country_iso_code = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'db_exchange'

class DbInterlistwatch(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    list_name = models.ForeignKey('DbListinter')
    instr_name = models.CharField(max_length=100, blank=True)
    instr_id = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'db_interlistwatch'

class DbListinter(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    name = models.CharField(max_length=120)
    class Meta:
        managed = False
        db_table = 'db_listinter'

class DbMynewswatchlist(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    list_name = models.CharField(max_length=120)
    class Meta:
        managed = False
        db_table = 'db_mynewswatchlist'

class DbNews(models.Model):
    id = models.IntegerField(primary_key=True)
    news_title = models.CharField(max_length=120)
    news_content = models.TextField()
    news_fasi = models.IntegerField()
    news_link = models.CharField(max_length=120)
    news_time = models.DateTimeField()
    source = models.CharField(max_length=120)
    instrument_id = models.ForeignKey('Instrument')
    incident = models.CharField(max_length=20)
    entity = models.CharField(max_length=20)
    industry_classification = models.ForeignKey('IndustryClassification')
    class Meta:
        managed = False
        db_table = 'db_news'

class DbNewsremind(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    last_search_time = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'db_newsremind'

class DbNewswatch(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    watch_list_name = models.ForeignKey(DbMynewswatchlist)
    source = models.CharField(max_length=120)
    entity = models.CharField(max_length=120)
    incident = models.CharField(max_length=120)
    class Meta:
        managed = False
        db_table = 'db_newswatch'

class DbWatchlist(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    watchlist_name = models.CharField(max_length=50)
    instrument = models.ForeignKey('Instrument', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'db_watchlist'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_migrations'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class DjceleryCrontabschedule(models.Model):
    id = models.IntegerField(primary_key=True)
    minute = models.CharField(max_length=64)
    hour = models.CharField(max_length=64)
    day_of_week = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=64)
    month_of_year = models.CharField(max_length=64)
    class Meta:
        managed = False
        db_table = 'djcelery_crontabschedule'

class DjceleryIntervalschedule(models.Model):
    id = models.IntegerField(primary_key=True)
    every = models.IntegerField()
    period = models.CharField(max_length=24)
    class Meta:
        managed = False
        db_table = 'djcelery_intervalschedule'

class DjceleryPeriodictask(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    task = models.CharField(max_length=200)
    interval = models.ForeignKey(DjceleryIntervalschedule, blank=True, null=True)
    crontab = models.ForeignKey(DjceleryCrontabschedule, blank=True, null=True)
    args = models.TextField()
    kwargs = models.TextField()
    queue = models.CharField(max_length=200, blank=True)
    exchange = models.CharField(max_length=200, blank=True)
    routing_key = models.CharField(max_length=200, blank=True)
    expires = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    last_run_at = models.DateTimeField(blank=True, null=True)
    total_run_count = models.IntegerField()
    date_changed = models.DateTimeField()
    description = models.TextField()
    class Meta:
        managed = False
        db_table = 'djcelery_periodictask'

class DjceleryPeriodictasks(models.Model):
    ident = models.SmallIntegerField(primary_key=True)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'djcelery_periodictasks'

class DjceleryTaskstate(models.Model):
    id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=64)
    task_id = models.CharField(max_length=36)
    name = models.CharField(max_length=200, blank=True)
    tstamp = models.DateTimeField()
    args = models.TextField(blank=True)
    kwargs = models.TextField(blank=True)
    eta = models.DateTimeField(blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    result = models.TextField(blank=True)
    traceback = models.TextField(blank=True)
    runtime = models.FloatField(blank=True, null=True)
    retries = models.IntegerField()
    worker = models.ForeignKey('DjceleryWorkerstate', blank=True, null=True)
    hidden = models.BooleanField()
    class Meta:
        managed = False
        db_table = 'djcelery_taskstate'

class DjceleryWorkerstate(models.Model):
    id = models.IntegerField(primary_key=True)
    hostname = models.CharField(max_length=255)
    last_heartbeat = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'djcelery_workerstate'

class Exchange(models.Model):
    id = models.IntegerField(primary_key=True)
    short_name = models.CharField(max_length=50, blank=True)
    long_name = models.CharField(max_length=50, blank=True)
    country_iso_code = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'exchange'

class FtrCustomerSentimentHourly(models.Model):
    date = models.DateField(blank=True, null=True)
    hour = models.SmallIntegerField(blank=True, null=True)
    instrument_id = models.CharField(max_length=6, blank=True)
    siteitemsraw_id = models.IntegerField(blank=True, null=True)
    customer_sentiment_raw_id = models.IntegerField(blank=True, null=True)
    polarity = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'ftr_customer_sentiment_hourly'

class FtrCustomerSentimentRaw(models.Model):
    id = models.IntegerField()
    customer_id = models.IntegerField(blank=True, null=True)
    scope_id = models.IntegerField(blank=True, null=True)
    ftr_event_raw_id = models.IntegerField(blank=True, null=True)
    polarity = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ftr_customer_sentiment_raw'

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

class FtrNewstagsRaw(models.Model):
    id = models.IntegerField(primary_key=True)
    news_id = models.IntegerField(blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=100, blank=True) # Field renamed because it was a Python reserved word.
    instance = models.CharField(max_length=100, blank=True)
    nlp_history_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ftr_newstags_raw'

class FtrNewstagsVw(models.Model):
    news_id = models.IntegerField(blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=100, blank=True) # Field renamed because it was a Python reserved word.
    instance = models.CharField(max_length=100, blank=True)
    nlp_history_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ftr_newstags_vw'

class Identifier(models.Model):
    id = models.IntegerField(primary_key=True)
    instrument_id = models.IntegerField(blank=True, null=True)
    identifier_type = models.CharField(max_length=10)
    identifier_value = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    currency_code = models.CharField(max_length=10)
    exchange = models.ForeignKey(DbExchange, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'identifier'

class IndustryClassification(models.Model):
    id = models.IntegerField(primary_key=True)
    classification_standard = models.CharField(max_length=50)
    classification_name = models.CharField(max_length=80)
    parent_classification = models.ForeignKey('self', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'industry_classification'

class Instrument(models.Model):
    id = models.IntegerField(primary_key=True)
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=100)
    instrument_type = models.CharField(max_length=50)
    issuer = models.ForeignKey('Issuer', blank=True, null=True)
    exchange = models.ForeignKey(DbExchange, blank=True, null=True)
    industry_classification = models.ForeignKey(IndustryClassification, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'instrument'

class Issuer(models.Model):
    id = models.IntegerField(primary_key=True)
    short_name = models.CharField(max_length=100, blank=True)
    long_name = models.CharField(max_length=100, blank=True)
    register_city = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'issuer'

class MarketPrice(models.Model):
    id = models.IntegerField(primary_key=True)
    instrument = models.ForeignKey(Instrument)
    datetime = models.DateTimeField()
    high_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    low_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    close_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    open_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'market_price'

class NewsDateStat(models.Model):
    d = models.DateField(blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'news_date_stat'

class NlpEventSubtype(models.Model):
    id = models.IntegerField()
    event_type = models.CharField(max_length=100, blank=True)
    event_type_id = models.IntegerField(blank=True, null=True)
    direction = models.CharField(max_length=100, blank=True)
    expectation = models.CharField(max_length=100, blank=True)
    expectation_bias = models.CharField(max_length=100, blank=True)
    sentiment = models.CharField(max_length=100, blank=True)
    event_subtype_description = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'nlp_event_subtype'

class NlpSchedulerConfig(models.Model):
    type = models.CharField(max_length=100)
    feature = models.CharField(max_length=100)
    table_name = models.CharField(max_length=50)
    column_name = models.CharField(max_length=50)
    gapp_version = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'nlp_scheduler_config'

class NlpSchedulerHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    news_id = models.IntegerField()
    gapp_version = models.CharField(max_length=50)
    execute_start_time = models.DateTimeField()
    execute_end_time = models.DateTimeField()
    execute_status = models.IntegerField()
    execute_msg = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'nlp_scheduler_history'

class OntoClass(models.Model):
    id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=100)
    parent_class_name = models.ForeignKey('self', blank=True, null=True)
    label = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'onto_class'

class OntoInstance(models.Model):
    id = models.IntegerField(primary_key=True)
    ontoclass = models.ForeignKey(OntoClass)
    instance_name = models.CharField(max_length=100)
    labels = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'onto_instance'

class OntoPropSpec(models.Model):
    id = models.IntegerField(primary_key=True)
    property_type = models.CharField(max_length=100)
    property_name = models.CharField(max_length=100)
    property_domain = models.ForeignKey(OntoClass)
    property_range = models.ForeignKey(OntoClass)
    class Meta:
        managed = False
        db_table = 'onto_prop_spec'

class OntoProperty(models.Model):
    id = models.IntegerField(primary_key=True)
    onto_instance = models.ForeignKey(OntoInstance)
    onto_property = models.ForeignKey(OntoPropSpec)
    property_instance = models.ForeignKey(OntoInstance)
    class Meta:
        managed = False
        db_table = 'onto_property'

class Price(models.Model):
    instrument_id = models.CharField(max_length=16, blank=True)
    date_time = models.DateTimeField(blank=True, null=True)
    open = models.TextField(blank=True) # This field type is a guess.
    high = models.TextField(blank=True) # This field type is a guess.
    low = models.TextField(blank=True) # This field type is a guess.
    close = models.TextField(blank=True) # This field type is a guess.
    volume = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'price'

class UserProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, unique=True)
    realname = models.CharField(max_length=150)
    mobile = models.CharField(max_length=11, blank=True)
    tel = models.CharField(max_length=13, blank=True)
    fax = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=30, blank=True)
    class Meta:
        managed = False
        db_table = 'user_profile'

class Watchlist(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    watchlist_name = models.CharField(max_length=50, blank=True)
    instrument = models.ForeignKey(Instrument, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'watchlist'

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

class WebSentimentHourly(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    hour = models.SmallIntegerField()
    instrument_id = models.CharField(max_length=16)
    sentiment = models.DecimalField(max_digits=25, decimal_places=2, blank=True, null=True)
    price = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'web_sentiment_hourly'

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

class WebTasklog(models.Model):
    celery_group = models.CharField(max_length=36)
    site = models.ForeignKey(WebFeedsites)
    modificationdatetimefield = models.DateTimeField(db_column='ModificationDateTimeField') # Field name made lowercase.
    task_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'web_tasklog'

class XxCustomerSentiment(models.Model):
    id = models.IntegerField()
    customer_id = models.IntegerField(blank=True, null=True)
    scope_id = models.IntegerField(blank=True, null=True)
    timestamp = models.TimeField(blank=True, null=True)
    polarity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'xx_customer_sentiment'

class XxFtrNewstagsRawTestonly(models.Model):
    id = models.IntegerField(primary_key=True)
    news_id = models.IntegerField(blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=100, blank=True) # Field renamed because it was a Python reserved word.
    nlp_history_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'xx_ftr_newstags_raw_testonly'

class XxNlpSchedulerHistory(models.Model):
    news_id = models.IntegerField()
    gapp_version = models.CharField(max_length=50)
    execute_start_time = models.DateTimeField()
    execute_end_time = models.DateTimeField()
    execute_status = models.IntegerField()
    execute_msg = models.TextField(blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'xx_nlp_scheduler_history'

