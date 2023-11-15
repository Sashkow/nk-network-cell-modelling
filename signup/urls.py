from django.urls import re_path
from signup import views


urlpatterns = [
    re_path(r"^$", views.get_name, name="get-name"),
    re_path(r"^thanks/$", views.thanks, name="thanks"),
]
