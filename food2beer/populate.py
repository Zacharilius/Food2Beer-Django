import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food2beer.settings')

import django
django.setup()

from food2beer_app.models import Brewery, Beer, Food
class Pop():
	def populate(self):

		union = self.add_brewery("Union", "Baltimore", "Maryland")
		self.add_beer("Duck Pin", union, "Pale Ale", 55, 5.5)
		self.add_beer("Balt Alt", union, "Alt", 45, 5.6)
		self.add_beer("Blackwing", union, "Black Lager", 27, 4.8)
		self.add_beer("Double Duck Pine", union, "Double IPA", 90, 8.5)
		self.add_beer("All American Classic", union, "Golden Ale", 35, 5.0)
		self.add_beer("Perfecta Pils", union, "Pilsner", 38, 5.4)


		gooseIsland = self.add_brewery("Goose Island", "Chicago", "Illinois")
		self.add_beer("312 Urban Wheat Ale", gooseIsland, 'Wheat Ale', 18, 4.2)
		self.add_beer("Honkers Ale", gooseIsland, 'English Style Bitter', 30, 4.3)
		
		heavySeas = self.add_brewery("Heavy Seas", "Baltimore", "Maryland")
		self.add_beer("Cross Bones", heavySeas, 'Session IPA', 35, 4.5)
		self.add_beer("Loose Cannon", heavySeas, 'American IPA', 45, 7.25)

		samAdams = self.add_brewery("Samual Adams", "Boston", "Massacheussetts")
		self.add_beer("Boston Lager", samAdams, 'Lager', 30, 4.9)


		harpoon = self.add_brewery("Harpoon", "Boston", "Massacheussetts")
		self.add_beer("IPA", harpoon, 'IPA', 42, 5.9)
		self.add_beer("Rye IPA", harpoon, 'Rye IPA', 70, 6.9)
		self.add_beer("UFO", harpoon, 'American White Ale', 11, 4.8)

		anchor = self.add_brewery("Anchor Brewing", "San Francisco", "California")
		self.add_beer("Anchor Steam Beer", anchor, 'Steam Beer', 37, 4.9)
		self.add_beer("California Lager", anchor, 'Lager', 6, 4.9)


		allagash = self.add_brewery("Allagash", "Portland", "Maine")
		self.add_beer("White", allagash, 'Belgian Wheat', 20, 5.0)

		greenFlash = self.add_brewery("Green Flash Brewing Company", "San Diego", "California")
		self.add_beer("Wes Coast IPA", greenFlash, 'IPA', 95, 8.1)


		victory = self.add_brewery("Victory Brewing Company", "Downington", "Pennsyolvania")
		self.add_beer("HopDevil IPA", victory, 'American IPA', 100, 6.7)
		self.add_beer("Storm King Stout", victory, 'American Imperial Stout', 65, 9.2)
		self.add_beer("Golden Monkey", victory, 'Belgian-Style Tripel', 25, 9.5)


		greatDivide = self.add_brewery("Great Divide Brewing Company", "Denver", "Colorado")
		self.add_beer("Claymore Scotch Ale", greatDivide, 'Belgian Wheat', 21, 7.7)
		self.add_beer("Denver Pale Ale", greatDivide, 'Pale Ale', 40, 5.5)

		dogfishHead = self.add_brewery("Dogfish Head", "Milton", "Delaware")
		self.add_beer("60 Minute", dogfishHead, 'IPA', 60, 6.0)

		self.add_food("Spicy")
		self.add_food("Chili")
		self.add_food("Burger")
		self.add_food("Carrot")
		self.add_food("Pork")
		self.add_food("Grill")
		self.add_food("Fish")
		self.add_food("Beef")
		self.add_food("Turkey")
		self.add_food("Salad")
		self.add_food("Seafood")
		self.add_food("Tilapia")
		self.add_food("Shrimp")
		self.add_food("Lobster")
		self.add_food("Taco")
		self.add_food("Mexican")
		self.add_food("Fruit")
		self.add_food("Vegetable")
		self.add_food("Bratwurst")
		self.add_food("Chicken")
		self.add_food("Spicy")
		self.add_food("Pork")
		self.add_food("Vegetable")
		self.add_food("Salmon")
		self.add_food("Herb")
		self.add_food("Sweet")
		self.add_food("Coffee")
		self.add_food("Smoked")
		self.add_food("Brisket")
		self.add_food("Jerk")
		self.add_food("Pepper")
		self.add_food("Suishi")
		self.add_food("Buffalo")
		self.add_food("Spiced")
		self.add_food("Mango")

		self.create_food2beer()

	def add_brewery(self, name, city, state):
		b = Brewery.objects.get_or_create(name=name, city=city, state=state)[0]
		b.save()
		self.breweryList.append(b)
		return b

	def add_beer(self, name, brewery, beerType, abv, ibus):
		b = Beer.objects.get_or_create(name = name, brewery = brewery, beerType = beerType, abv = abv, ibus = ibus)[0]
		b.save()
		self.beerList.append(b)

	def add_food(self, name):
		f = Food.objects.get_or_create(name = name)[0]
		f.save()
		self.foodList.append(f)	

	def create_food2beer(self):
		self.food2beer["Spicy"] = "IPA"
		self.food2beer["Chili"] = "IPA"
		self.food2beer["Burger"] = "IPA"
		self.food2beer["Carrot"] = "IPA"

		self.food2beer["Spicy"] = "Imperial IPA"
		self.food2beer["Chili"] = "Imperial IPA"
		self.food2beer["Burger"] = "Imperial IPA"
		self.food2beer["Carrot"] = "Imperial IPA"

		self.food2beer["Pork"] = "Porter"
		self.food2beer["Grill"] = "Porter"
		self.food2beer["Fish"] = "Porter"
		self.food2beer["Beef"] = "Porter"
		self.food2beer["Turkey"] = "Porter"
		self.food2beer["Sweet"] = "Porter"

		self.food2beer["Pork"] = "Stout"
		self.food2beer["Grill"] = "Stout"
		self.food2beer["Fish"] = "Stout"
		self.food2beer["Beef"] = "Stout"
		self.food2beer["Turkey"] = "Stout"
		self.food2beer["Sweet"] = "Stout"
		self.food2beer["Coffee"] = "Stout"
		self.food2beer["Caramel"] = "Stout"

		self.food2beer["Salad"] = "Hefeweizen"
		self.food2beer["Seafood"] = "Hefeweizen"
		self.food2beer["Tilapia"] = "Hefeweizen"
		self.food2beer["Shrimp"] = "Hefeweizen"
		self.food2beer["Lobster"] = "Hefeweizen"
		self.food2beer["Taco"] = "Hefeweizen"
		self.food2beer["Mexican"] = "Hefeweizen"
		self.food2beer["Fruit"] = "Hefeweizen"
		self.food2beer["Vegetable"] = "Hefeweizen"
		self.food2beer["Sweet"] = "Porter"


		self.food2beer["Bratwurst"] = "Amber Ale"
		self.food2beer["Chicken"] = "Amber Ale"
		self.food2beer["Burgers"] = "Amber Ale"
		self.food2beer["Spicy"] = "Amber Ale"
		self.food2beer["Pork"] = "Amber Ale"
		self.food2beer["Smoked"] = "Amber Ale"


		self.food2beer["Pork"] = "Brown Ale"
		self.food2beer["Salmon"] = "Brown Ale"
		self.food2beer["Grill"] = "Brown Ale"
		self.food2beer["Burger"] = "Brown Ale"
		self.food2beer["Brisket"] = "Brown Ale"
		self.food2beer["Sausage"] = "Brown Ale"
		self.food2beer["Peanut"] = "Brown Ale"
		self.food2beer["Nut"] = "Brown Ale"


		self.food2beer["Pork"] = "Pilsner"
		self.food2beer["Fish"] = "Pilsner"
		self.food2beer["Chicken"] = "Pilsner"
		self.food2beer["Vegetable"] = "Pilsner"
		self.food2beer["Salmon"] = "Pilsner"

		self.food2beer["Mexican"] = "Pale Ale"
		self.food2beer["Curry"] = "Pale Ale"
		self.food2beer["Sweet"] = "Pale Ale"
		self.food2beer["Spiced"] = "Pale Ale"

		self.food2beer["Seafood"] = "Witbier"
		self.food2beer["Ceviche"] = "Witbier"
		self.food2beer["Citrus"] = "Witbier"

		self.food2beer["Herb"] = "Saison"
		self.food2beer["Chicken"] = "Saison"

		self.food2beer["Pork"] = "English Style Bitter"

		self.food2beer["Burger"] = "Alt"

		self.food2beer["Lemon"] = "Lager"
		self.food2beer["Spicy"] = "Lager"
		self.food2beer["Asian"] = "Lager"
		self.food2beer["Tuna"] = "Lager"
		self.food2beer["Tomato"] = "Lager"
		self.food2beer["Cajun"] = "Lager"
		self.food2beer["Jerk"] = "Lager"
		self.food2beer["Spice"] = "Lager"

		self.food2beer["Italian"] = "Golden Ale"
		self.food2beer["Spaghetti"] = "Golden Ale"
		self.food2beer["Shellfish"] = "Golden Ale"

		self.food2beer["Asian"] = "Blonde Ale"
		self.food2beer["Jalapeno"] = "Blonde Ale"
		self.food2beer["Mango"] = "Blonde Ale"
		self.food2beer["Salsa"] = "Blonde Ale"
		self.food2beer["Chili"] = "Blonde Ale"

		self.food2beer["Garlic"] = "Wheat Ale"
		self.food2beer["Scallops"] = "Wheat Ale"
		self.food2beer["Shrimp"] = "Wheat Ale"

		self.food2beer["Bacon"] = "Rye IPA"

		self.food2beer["Suishi"] = "American White Ale"
		self.food2beer["Buffalo"] = "American White Ale"


		self.food2beer["Pepper"] = "Belgian-Style Tripel"

		self.food2beer["Pepper"] = "Belgian Wheat"

		self.food2beer["Mexican"] = "Marzen"

		self.food2beer["Mexican"] = "Oktoberfest"

		self.food2beer["Cajun"] = "Bock"
		self.food2beer["Jerk"] = "Bock"

		#print self.food2beer
		for food in Food.objects.all():
			#print  food
			for beer in Beer.objects.all():
				#print beer.beerType
				#print self.food2beer[str(food)]
				if beer.beerType  == self.food2beer[str(food)]:
					food.beer.add(beer)
	def __init__(self):
		# Delete all entries in database
		Beer.objects.all().delete()
		Brewery.objects.all().delete()
		Food.objects.all().delete()

		# Create lists
		self.breweryList = []
		self.foodList = []
		self.beerList = []
		self.food2beer = {}
		print "Starting population script for Food2Beer..."

		self.populate()

		print ""
		allPairs = Food.objects.all()
		print allPairs[0].beer
		print ""
		print "Finished populating Food2Beer"

Pop()