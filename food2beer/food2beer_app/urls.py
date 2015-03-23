from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from food2beer_app.models import Brewery

urlpatterns = patterns('',
	# Brewery List	
	url(r'^(?P<page>\d+)?/?$', ListView.as_view(
		model=Brewery,
		paginate_by=5,
		)),
	# Individual brewery
	url(r'^(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(
		model=Brewery,
		)),

)
