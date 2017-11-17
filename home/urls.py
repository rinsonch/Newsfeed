from django.conf.urls import url

from home import views

from django.contrib import admin
from django.contrib.auth import views as auth_views
app_name='home'

urlpatterns = [
    url(r'^signup/$',views.signup , name='signup'),
    url(r'^$', auth_views.login, {'template_name': 'home/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'template_name':'login.html'},name='logout'),
]