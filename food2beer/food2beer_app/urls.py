from django.conf.urls import patterns, url
from django.views.generic import ListView
from food2beer_app.models import Brewery

urlpatterns = patterns('',
	
	url(r'^(?P<page>\d+)?/?$', ListView.as_view(
		model=Brewery,
		paginate_by=5,
		)),
)
