from django.conf.urls import patterns, include, url
from django.contrib import admin
from signup import views

urlpatterns = patterns('',
    url(r'^$', views.get_name, name='get-name'),
    url(r'^thanks/$', views.thanks, name='thanks')
)
