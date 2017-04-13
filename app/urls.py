from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.rest_index, name='rest_index'),
    url(r'^new/$', views.rest_new, name='rest_new'),
]
