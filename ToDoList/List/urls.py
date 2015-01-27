from django.conf.urls import patterns, url
from List import views

urlpatterns = patterns('',

	url(r'^$', views.index, name='index'),
	url('list/$', views.list, name='list'),


    #copy paste the below for testing...
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/login/$', 'views.login'),
    url(r'^accounts/auth/$', 'views.auth_view'),
    url(r'^accounts/logout/$', 'views.logout'),
    url(r'^accounts/loggedin/$', 'views.loggedin'),
    url(r'^accounts/invalid/$', 'views.invalid_login'),
)