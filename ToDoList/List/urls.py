from django.conf.urls import patterns, url
#import List.views
from List import views


urlpatterns = patterns('List.views',
	url(r'^$', views.index, name='index'),
	url(r'^list/complete/$', views.complete, name='complete'),
	url(r'^list/$', views.list, name='list'),
	url(r'^register/$', views.register, name='register'),
	#url(r'^list/item/(?P<task_id>\d+)/$', views.item, name='item'),
)