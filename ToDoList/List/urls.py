from django.conf.urls import patterns, url
#import List.views
from List import views


urlpatterns = patterns('List.views',
	url(r'^$', views.index, name='index'),
	#url('list/$', views.list, name='list'),
	url(r'^list/$', views.list, name='list'),
	url(r'^item/(?P<task_id>\d+)/$', views.item, name='item'),
)