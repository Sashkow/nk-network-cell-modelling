from django.conf.urls import patterns, include, url
from django.contrib import admin
from graphs import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cell_modelling_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index,name='index'),
    url(r'^(?P<N>[0-9]+)/(?P<K>[0-9]+)/$',views.index,name='index'),
    url(r'^build/$',views.build,name='build'),
    url(r'^build_ajax/$',views.build_ajax,name='build-ajax'),
    url(r'^message/$',views.message, name='message'),
    url(r'^image/(?P<graph_name>[a-z_a-z]+)/$', views.dynamic_image, name='dynamic-image'),    
    url(r'^image/(?P<cell_id>[0-9]+)/(?P<graph_name>[a-z_a-z]+)/$', views.dynamic_image_by_cell_id, name='dynamic-image-by-cell-id'),    
    url(r'^like/$',views.like,name='like'),
    url(r'^cells_top_list/$',views.show_most_liked_cells,name='cells-top-list')
)
