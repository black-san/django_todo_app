from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^delete/(?P<list_id>[\d-]+)/$', views.delete, name="delete"),
    url(r'^\Z', views.home, name="home"),
    url(r'^delete/', views.delete, name="delete")
]