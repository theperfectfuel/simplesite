from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'simplesite.views.home', name='home'),
    url(r'^about/$', 'simplesite.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #Auth related urls
    url(r'^accounts/login/$', 'simplesite.views.login', name='login'),
    url(r'^accounts/logout/$', 'simplesite.views.loggedin', name='logout'),
    url(r'^accounts/loggedin/$', 'simplesite.views.loggedin', name='loggedin'),

)
