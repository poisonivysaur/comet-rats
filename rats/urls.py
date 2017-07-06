from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/profile/$', views.toHomeURL, name='homeURL'),
    url(r'^toLoginURL/$', views.toLoginURL, name='toLoginURL'),
    url(r'^home', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    
    url(r'^residency/$', views.residency, name='residency'),
    url(r'^residency/new/$', views.res_new, name='res_new'),
    url(r'^residency/(?P<pk>\d+)/$', views.res_detail, name='res_detail'),
    url(r'^residency/(?P<pk>\d+)/edit/$', views.res_edit, name='res_edit'),
    url(r'^residency/(?P<pk>\d+)/remove/$', views.res_remove, name='res_remove'),

    url(r'^attendance/$', views.attendance, name='attendance'),
    url(r'^attendance/new/$', views.att_new, name='att_new'),
    url(r'^attendance/(?P<pk>\d+)/$', views.att_detail, name='att_detail'),
    url(r'^attendance/(?P<pk>\d+)/edit/$', views.att_edit, name='att_edit'),
    url(r'^attendance/(?P<pk>\d+)/remove/$', views.att_remove, name='att_remove'),

    url(r'^teams/$', views.teams, name='teams'),
    url(r'^teams/new/$', views.team_new, name='team_new'),
    url(r'^teams/(?P<pk>\d+)/$', views.team_detail, name='team_detail'),
    url(r'^teams/(?P<pk>\d+)/edit/$', views.team_edit, name='team_edit'),
    url(r'^teams/(?P<pk>\d+)/remove/$', views.team_remove, name='team_remove'),

    url(r'^projects/$', views.projects, name='projects'),
    url(r'^projects/new/$', views.proj_new, name='proj_new'),
    url(r'^projects/(?P<pk>\d+)/$', views.proj_detail, name='proj_detail'),
    url(r'^projects/(?P<pk>\d+)/edit/$', views.proj_edit, name='proj_edit'),
    url(r'^projects/(?P<pk>\d+)/remove/$', views.proj_remove, name='proj_remove'),
    
]
