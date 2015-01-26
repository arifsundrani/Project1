from django.conf.urls import patterns, url
from List import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url('list/$', views.list, name='list'),
)