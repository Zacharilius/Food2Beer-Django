from django.conf.urls import patterns, url
from food2beer_app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'))
