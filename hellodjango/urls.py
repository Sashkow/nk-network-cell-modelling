from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Examples:
    # path('', 'hellodjango.views.home', name='home'),
    # path('blog/', include('blog.urls')),
    path('', include('graphs.urls')),
    path('graphs/', include('graphs.urls')),
    path('signup/', include('signup.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
]
