#!/usr/bin/env python
# coding: utf-8

from django.contrib import admin
from apps.db.models import (Issuer, IssuerAdmin, Instrument, InstrumentAdmin,
        Exchange, ExchangeAdmin, IndustryClassification,
        IndustryClassificationAdmin, Country, CountryAdmin,
        Identifier, IdentifierAdmin, Price, PriceAdmin,
        Customer, CustomerAdmin, Watchlist, WatchlistAdmin, News, NewsAdmin,
        Interlistwatch, InterlistwatchAdmin, Listinter, ListinterAdmin,
        Newswatch, NewswatchAdmin, MynewswatchList, MynewswatchListAdmin,
        NewsRemind, NewsRemindAdmin
        )

admin.site.register(Issuer, IssuerAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Exchange, ExchangeAdmin)
admin.site.register(IndustryClassification, IndustryClassificationAdmin)
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
