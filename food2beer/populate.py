import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food2beer.settings')

import django
django.setup()

from food2beer_app.models import Brewery

def populate():
	add_brewery("Union", "Baltimore", "Maryland")
	add_brewery("Goose Island", "Chicago", "Illinois")
	add_brewery("Heavy Seas", "Baltimore", "Maryland")
	add_brewery("Samual Adams", "Boston", "Massacheussetts")
	add_brewery("Harpoon", "Boston", "Massacheussetts")
	add_brewery("Avondale Brewing Company", "Birmingham", "Alabama")
	add_brewery("Back Forty Beer Company", "Gadsden", "Alabama")
	add_brewery("Beer Engineers", "Birmingham", "Alabama")
	add_brewery("Below the Radar Brewhouse", "Huntsville", "Alabama")
	add_brewery("Cahaba Brewing Company", "Birmingham", "Alabama")
	add_brewery("Druid City Brewery Company", "Tuscaloosa", "Alabama")

def add_brewery(name, city, state):
	b = Brewery.objects.get_or_create(name=name, city=city, state=state)[0]
	b.save()
	return b

if __name__ == '__main__':
	print "Starting population script for Food2Beer..."
	populate()
