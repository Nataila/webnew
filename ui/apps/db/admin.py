#!/usr/bin/env python
# coding: utf-8

from django.contrib import admin
from apps.db.models import (Issuser, IssuerAdmin, Instrument, InstrumentAdmin,
        Exchange, ExchangeAdmin, Industry_classification,
        Industry_classificationAdmin, Country, CountryAdmin,
        Identifier, IdentifierAdmin, Price, PriceAdmin,
        Customer, CustomerAdmin, Watchlist, WatchlistAdmin, News, NewsAdmin,
        Interlistwatch, InterlistwatchAdmin, Listinter, ListinterAdmin,
        Newswatch, NewswatchAdmin, MynewswatchList, MynewswatchListAdmin,
        NewsRemind, NewsRemindAdmin
        )

admin.site.register(Issuser, IssuerAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Exchange, ExchangeAdmin)
admin.site.register(Industry_classification, Industry_classificationAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Identifier, IdentifierAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Interlistwatch, InterlistwatchAdmin)
admin.site.register(Listinter, ListinterAdmin)
admin.site.register(Newswatch, NewswatchAdmin)
admin.site.register(MynewswatchList, MynewswatchListAdmin)
admin.site.register(NewsRemind, NewsRemindAdmin)
