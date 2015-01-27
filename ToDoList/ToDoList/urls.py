from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ToDoList.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^List/', include('List.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/login/$', 'views.login'),
    url(r'^accounts/auth/$', 'views.auth_view'),
    url(r'^accounts/logout/$', 'views.logout'),
    url(r'^accounts/loggedin/$', 'views.loggedin'),
    url(r'^accounts/invalid/$', 'views.invalid_login'),
)
