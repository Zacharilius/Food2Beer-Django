from django.test import TestCase, LiveServerTestCase, Client
from food2beer_app.models import Beer, Brewery

import factory.django

class BreweryFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Brewery
		django_get_or_create = (
			'name',
			'city',
			'state'
		)
	name = 'Heavy Seas'
	city = 'Baltimore'
	state = 'Maryland'

class BeerFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Beer
		django_get_or_create = (
			'name',
			'brewery'
		)
	name = 'Loose Cannon'
	brewery = factory.SubFactory(BreweryFactory)

class PreTest(TestCase):
	def test_create_brewery(self):
		brewery = BreweryFactory()

		# Checks for brewery test initiated correctly
		all_breweries = Brewery.objects.all()
		self.assertEquals(len(all_breweries), 1)
		only_brewery = all_breweries[0]
		self.assertEquals(only_brewery, brewery)

		# Makes sures attributes are correctly initiated
		self.assertEquals(only_brewery.name, 'Heavy Seas')
		self.assertEquals(only_brewery.city, 'Baltimore')
		self.assertEquals(only_brewery.state, 'Maryland')

	def test_create_beer(self):
		# Creates instances of brewery and beer
		brewery = BreweryFactory()
		beer = BeerFactory()

		# Checks that beer was initiated correctly
		all_beers = Beer.objects.all()
		self.assertEquals(len(all_beers),1)
		only_beer = all_beers[0]
		self.assertEquals(only_beer, beer)

		# Makes sure attributes are correctly initiated
		self.assertEquals(only_beer.name, 'Loose Cannon')
		self.assertEquals(only_beer.brewery.name, 'Heavy Seas')

