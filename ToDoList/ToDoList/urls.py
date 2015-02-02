from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ToDoList.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('List.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    
   url(r'^accounts/login/$', 'ToDoList.views.login'),
    url(r'^accounts/auth/$', 'ToDoList.views.auth_view'),
    url(r'^accounts/logout/$', 'ToDoList.views.logout'),
    url(r'^accounts/loggedin/$', 'ToDoList.views.loggedin'),
    url(r'^accounts/invalid/$', 'ToDoList.views.invalid_login'),
    
)
