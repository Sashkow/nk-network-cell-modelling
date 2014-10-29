from django.conf.urls import patterns, include, url
from django.contrib import admin
from graphs import views

print "in graphs/urls.py"
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cell_modelling_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index,name='index'),
    url(r'^build/$',views.build,name='build'),
    url(r'^message/$',views.message, name='message'),
    
)
