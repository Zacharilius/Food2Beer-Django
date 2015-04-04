import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food2beer.settings')

import django
django.setup()

from food2beer_app.models import Brewery, Beer

def populate():
	union = add_brewery("Union", "Baltimore", "Maryland")
	add_beer("Duck Pin", union, "Pale Ale", 55, 5.5)
	add_beer("Balt Alt", union, "Alt", 45, 5.6)
	add_beer("Blackwing", union, "Black Lager", 27, 4.8)
	add_beer("Double Duck Pine", union, "Double IPA", 90, 8.5)
	add_beer("All American Classic", union, "Golden Ale", 35, 5.0)
	add_beer("Perfecta Pils", union, "Pilsner", 38, 5.4)


	gooseIsland = add_brewery("Goose Island", "Chicago", "Illinois")
	add_beer("312 Urban Wheat Ale", gooseIsland, 'Wheat Ale', 18, 4.2)
	add_beer("Honkers Ale", gooseIsland, 'English Style Bitter', 30, 4.3)
	
	heavySeas = add_brewery("Heavy Seas", "Baltimore", "Maryland")
	add_beer("Cross Bones", heavySeas, 'Session IPA', 35, 4.5)
	add_beer("Loose Cannon", heavySeas, 'American IPA', 45, 7.25)

	samAdams = add_brewery("Samual Adams", "Boston", "Massacheussetts")
	add_beer("Boston Lager", samAdams, 'Lager', 30, 4.9)


	harpoon = add_brewery("Harpoon", "Boston", "Massacheussetts")
	add_beer("IPA", harpoon, 'IPA', 42, 5.9)
	add_beer("Rye IPA", harpoon, 'Rye IPA', 70, 6.9)
	add_beer("UFO", harpoon, 'American White Ale', 1, 4.8)

	anchor = add_brewery("Anchor", "San Francisco", "California")
	allagash = add_brewery("Allagash", "Portland", "Maine")
	greenFlash = add_brewery("Green Flash Brewing Company", "San Diego", "California")
	victory = add_brewery("Victory Brewing Company", "Downington", "Pennsyolvania")
	greatDivide = add_brewery("Great Divide Brewing Company", "Denver", "Colorado")
	dogfishHead = add_brewery("Dogfish Head", "Milton", "Delaware")


def add_brewery(name, city, state):
	b = Brewery.objects.get_or_create(name=name, city=city, state=state)[0]
	b.save()
	return b

def add_beer(name, brewery, beerType, abv, ibus):
	b = Beer.objects.get_or_create(name = name, brewery = brewery, beerType = beerType, abv = abv, ibus = ibus)[0]
	b.save()

if __name__ == '__main__':
	print "Starting population script for Food2Beer..."
	populate()
