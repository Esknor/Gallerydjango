from django.conf.urls import include, url

from . views import (
  post_list,
  post_create,
  post_detail,
  post_update,
  post_delete,
  title,
)

urlpatterns = [
  url(r'^$', title, name='title'),
  url(r'^post_list/$', post_list, name='post_list'),
  url(r'^post_create/$', post_create, name='post_create'),
  url(r'^(?P<slug>[\w-]+)/$', post_detail, name='post_detail'),
  url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='post_update'),
  url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='post_delete'),
]
