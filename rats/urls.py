from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/profile/$', views.homeURL, name='homeURL'),
    url(r'^home', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^attendance/$', views.attendance, name='attendance'),
    url(r'^residency/$', views.residency, name='residency'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^teams/$', views.teams, name='teams'),
    
]