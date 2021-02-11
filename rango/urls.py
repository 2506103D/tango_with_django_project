# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 20:40:35 2021

@author: rachd
"""

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
        path('', views.index, name='index'),
]