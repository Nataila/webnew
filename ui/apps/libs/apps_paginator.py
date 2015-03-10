#!/usr/bin/env python
# coding=utf-8


from django.core.paginator import EmptyPage
from django.core.paginator import InvalidPage
from django.core.paginator import Paginator


def get_paged_items(source_items, cur_page_num, num_per_page=50, show_paginator=False):
    """获取某个列表分页后的列表"""

    paginator = Paginator(source_items, num_per_page)
    try:
        page = int(cur_page_num)
    except ValueError:
        page = 1

    try:
        paged_items = paginator.page(page)
    except (EmptyPage, InvalidPage):
        paged_items = paginator.page(paginator.num_pages)

    if show_paginator:
        return paged_items, paginator
    else:
        return paged_items
