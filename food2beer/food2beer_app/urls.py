from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView

from food2beer_app.models import Brewery, Beer
from food2beer_app.views import BreweryListView
from food2beer_app import views

urlpatterns = patterns('',
	# Beer List	
	url(r'^beer-list/(?P<page>\d+)?/?$', ListView.as_view(
		model=Beer,
		paginate_by=5,
		)),
	# Individual beer
	url(r'^beer/(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(
		model=Beer,
		)),
	
	# Brewery category
	url(r'^brewery/(?P<slug>[a-zA-Z0-9-]+)/?$', BreweryListView.as_view(
		paginate_by=5,
		model=Brewery,
		)),

	# Breweries List
	url(r'^breweries/(?P<page>\d+)?/?$', ListView.as_view(
		paginate_by=5,
		model=Brewery,
		)),
	url(r'^$', views.food2beer, name='food2beer'),
)
