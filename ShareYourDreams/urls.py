from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dreams_list, name='dreams_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.dream_detail, name='dream_detail'),
    url(r'^post/new/$', views.dream_new, name='dream_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.dream_edit, name='dream_edit'),
    url(r'^registration', views.registration, name='registration'),
]
