from django.shortcuts import render
from django.views.generic import ListView

from food2beer_app.models import Brewery, Beer


class BreweryListView(ListView):
	def get_queryset(self):
		slug = self.kwargs['slug']
		try:
			brewery = Brewery.objects.get(slug=slug)
			return Beer.objects.filter(brewery=brewery)
		except Brewery.DoesNotExist:
			return Beer.objects.none()
