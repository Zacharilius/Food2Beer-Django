from django.test import TestCase, LiveServerTestCase, Client
from food2beer_app.models import Beer, Brewery

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
	pass
