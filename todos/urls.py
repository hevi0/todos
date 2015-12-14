from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.TodosView.as_view(), name='todos-list'),
    url(r'^(?P<todos_id>[0-9]+)/$', views.TodosView.as_view(), name='todos-detail'),
    url(r'^(?P<todos_id>[0-9]+)/items/(?P<todoitem_id>[0-9]+)/$', views.TodoItemView.as_view(), name='items-detail'),
    url(r'^(?P<todos_id>[0-9]+)/items/$', views.TodoItemView.as_view(), name='items-list'),


]
