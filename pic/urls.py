#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/5/17 17:21
# @Author  : dreamgc
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.get_pic, name='get_pic'),
    path('add/', views.add_pic, name='add_pic')
]
