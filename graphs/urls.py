from django.contrib import admin
from django.urls import include, path, re_path
from graphs import views

urlpatterns = [
    # Examples:
    # path('', 'cell_modelling_site.views.home', name='home'),
    # path('blog/', include('blog.urls')),
    path('', views.index, name="index"),
    re_path(r"^(?P<N>[0-9]+)/(?P<K>[0-9]+)/$", views.index, name="index"),
    path("build/", views.build, name="build"),
    path("build_ajax/", views.build_ajax, name="build-ajax"),
    path("message/", views.message, name="message"),
    re_path(r"^image/(?P<graph_name>[a-z_a-z]+)/$", views.dynamic_image, name="dynamic-image"),
    re_path(
        r"^image/(?P<cell_id>[0-9]+)/(?P<graph_name>[a-z_a-z]+)/$",
        views.dynamic_image_by_cell_id,
        name="dynamic-image-by-cell-id",
    ),
    path("like/", views.like, name="like"),
    path("cells_top_list/", views.show_most_liked_cells, name="cells-top-list"),
]
