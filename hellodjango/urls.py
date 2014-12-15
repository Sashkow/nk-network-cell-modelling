from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',include('graphs.urls')),
    url(r'^graphs/',include('graphs.urls')),
    url(r'^signup/',include('signup.urls')),
    url(r'^admin/', include(admin.site.urls)),

    
)
