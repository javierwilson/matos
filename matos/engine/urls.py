# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_viewa

from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^operation/$', views.operation_list),
    url(r'^operation/(?P<pk>[0-9]+)$', views.operation_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
