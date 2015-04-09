import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food2beer.settings')

import django
django.setup()

from food2beer_app.models import Brewery, Beer, Food
class Pop():
	def populate(self):
		# Add beers and breweries
		self.add_beerBreweries_db()

		# Add 
		self.add_foods_db()


		self.create_food2beer()


	def add_beerBreweries_db(self):
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
		self.add_beer("Loose Cannon", heavySeas, 'IPA', 45, 7.25)

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


		victory = self.add_brewery("Victory Brewing Company", "Downington", "Pennsylvania")
		self.add_beer("HopDevil IPA", victory, 'American IPA', 100, 6.7)
		self.add_beer("Storm King Stout", victory, 'American Imperial Stout', 65, 9.2)
		self.add_beer("Golden Monkey", victory, 'Belgian-Style Tripel', 25, 9.5)


		greatDivide = self.add_brewery("Great Divide Brewing Company", "Denver", "Colorado")
		self.add_beer("Claymore Scotch Ale", greatDivide, 'Belgian Wheat', 21, 7.7)
		self.add_beer("Denver Pale Ale", greatDivide, 'Pale Ale', 40, 5.5)

		dogfishHead = self.add_brewery("Dogfish Head", "Milton", "Delaware")
		self.add_beer("60 Minute", dogfishHead, 'IPA', 60, 6.0)

		guinness = self.add_brewery("Guinness", "Dublin", "Ireland")
		self.add_beer("Extra Stout", guinness, 'Stout', 22, 6.0)

		newcastle = self.add_brewery("Newcastle", "Tadcaster", "United Kingdom")
		self.add_beer("Brown Ale", newcastle, 'Brown Ale', 18.5, 4.7)

		phillyBrewCo = self.add_brewery("Philadelphia Brewing Company", "Philadelphia", "Pennsylvania")
		self.add_beer("Walt Wit", phillyBrewCo, 'Witbier', 20, 4.5)
		self.add_beer("Kenzinger", phillyBrewCo, 'Pilsner', 33, 4.5)
		self.add_beer("Schwarzinger", phillyBrewCo, 'Black Lager', 20, 5.0)
	
		sierraNevada = self.add_brewery("Sierra Nevada", "Chico", "California")
		self.add_beer("Kellerweis", sierraNevada, 'Hefeweizen', 15, 4.8)



	def add_foods_db(self):
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
		self.add_food("Sweet")
		self.add_food("Smoked")
		self.add_food("Peanut")
		self.add_food("Nut")
		self.add_food("Fish")
		self.add_food("Curry")
		self.add_food("Seafood")
		self.add_food("Ceviche")
		self.add_food("Citrus")
		self.add_food("Herb")
		self.add_food("Lemon")
		self.add_food("Asian")
		self.add_food("Tuna")
		self.add_food("Cajun")
		self.add_food("Jerk")
		self.add_food("Italian")
		self.add_food("Spaghetti")
		self.add_food("Shellfish")
		self.add_food("Asian")
		self.add_food("Garlic")
		self.add_food("Scallops")
		self.add_food("Shrimp")
		self.add_food("Bacon")
		self.add_food("Suishi")
		self.add_food("Buffalo")
		self.add_food("Pepper")
		self.add_food("Mexican")
		self.add_food("Nachos")
		self.add_food("Chorizo")
		self.add_food("Falafel")
		self.add_food("Grapefruit")
		self.add_food("Samosas")
		self.add_food("Fried")
		self.add_food("Goose")
		self.add_food("Hamburger")
		self.add_food("Pizza")
		self.add_food("Gumbo")
		self.add_food("Calamari")
		self.add_food("Pasta")
		self.add_food("Risotto")
		self.add_food("Octopus")
		self.add_food("Pesto")
		self.add_food("Ratatouille")
		self.add_food("Anchiovies")
		self.add_food("Bruschetta")
		self.add_food("Caviar")
		self.add_food("Chinese")
		self.add_food("Chorizo")
		self.add_food("Barbecue")
		self.add_food("Halibut")
		self.add_food("Omelet")
		self.add_food("Macaroni")
		self.add_food("Rabbit")
		self.add_food("Quail")
		self.add_food("Meatloaf")
		self.add_food("Sausage")
		self.add_food("Pheasant")
		self.add_food("Monkfish")
		self.add_food("Crab")
		self.add_food("Halibut")
		self.add_food("Mozzarella")
		self.add_food("Goat")
		self.add_food("Salami")




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
		self.food2beer["Anchiovies"] = ["Pilsner"]

		self.food2beer["Asian"] = ["Lager"]
		self.food2beer["Bacon"] = ["Rye IPA"]
		self.food2beer["Barbecue"] = ["Wheat Ale"]

		self.food2beer["Beef"] = ["Porter", 'Stout']
		self.food2beer["Bratwurst"] = ["Amber Ale"]
		self.food2beer["Brisket"] = ["Brown Ale"]
		self.food2beer["Bruschetta"] = ["Pilsner"]

		self.food2beer["Buffalo"] = ["American White Ale"]
		self.food2beer["Burger"] = ["Alt", "Pilsner", "Amber Ale"]
		self.food2beer["Calamari"] = ["Black Lager"]

		self.food2beer["Cajun"] = ["Lager", "Bock"]
		self.food2beer["Caramel"] = ["Stout"]
		self.food2beer["Carrot"] = ["Rye IPA"]
		self.food2beer["Caviar"] = ["Pilsner"]

		self.food2beer["Ceviche"] = ["Witbier"]
		self.food2beer["Citrus"] = ["Witbier"]
		self.food2beer["Chicken"] = ["Black Lager", "Belgian-Style Tripel"]
		self.food2beer["Chili"] = ["IPA", "American IPA", "Double IPA"]
		self.food2beer["Chinese"] = ["Pilsner"]
		self.food2beer["Chorizo"] = ["Pilsner", "Pale Ale"]

		self.food2beer["Coffee"] = ["Stout"]
		self.food2beer["Crab"] = ["Session IPA"]

		self.food2beer["Curry"] = ["Pale Ale"]
		self.food2beer["Falafel"] = ["Pale Ale"]
		self.food2beer["Fish"] = ["Porter", 'Stout', 'Pilsner']
		self.food2beer["Fried"] = ["Alt"]

		self.food2beer["Fruit"] = ["Hefeweizen"]
		self.food2beer["Garlic"] = ["Wheat Ale"]
		self.food2beer["Goat"] = ["Belgian Wheat"]

		self.food2beer["Goose"] = ["Alt"]

		self.food2beer["Grapefruit"] = ["Pale Ale"]

		self.food2beer["Grill"] = ["Porter", "Stout", "Brown Ale"]
		self.food2beer["Gumbo"] = ["Black Lager"]

		self.food2beer["Hamburger"] = ["Alt"]
		self.food2beer["Halibut"] = ["Wheat Ale"]

		self.food2beer["Herb"] = ["Saison"]
		self.food2beer["Italian"] = ["Golden Ale"]
		self.food2beer["Jalapeno"] = ["Blonde Ale"]

		self.food2beer["Jerk"] = ["Steam Beer"]
		self.food2beer["Lemon"] = ["Hefeweizen"]

		self.food2beer["Lobster"] = ["Hefeweizen"]
		self.food2beer["Macaroni"] = ["English Style Bitter"]

		self.food2beer["Mango"] = ["Blonde Ale"]
		self.food2beer["Meatloaf"] = ["English Style Bitter"]

		self.food2beer["Mexican"] = ["Hefeweizen", "Pale Ale", "Marzen","Oktoberfest"]
		self.food2beer["Monkfish"] = ["English Style Bitter"]
		self.food2beer["Mozzarella"] = ["Belgian Wheat"]
		self.food2beer["Nachos"] = ["Pale Ale"]

		self.food2beer["Nut"] = ["Brown Ale"]
		self.food2beer["Octopus"] = ["Golden Ale"]
		self.food2beer["Omelet"] = ["Wheat Ale"]
		self.food2beer["Quail"] = ["English Style Bitter"]

		self.food2beer["Pasta"] = ["Golden Ale"]

		self.food2beer["Peanut"] = ["Brown Ale"]
		self.food2beer["Pepper"] = ["Belgian-Style Tripel", "Belgian Wheat"]
		self.food2beer["Pesto"] = ["Golden Ale"]
		self.food2beer["Pheasant"] = ["English Style Bitter"]

		self.food2beer["Pizza"] = ["Black Lager"]

		self.food2beer["Pork"] = ["Porter", "Stout", "English Style Bitter"]
		self.food2beer["Rabbit"] = ["English Style Bitter"]

		self.food2beer["Ratatouille"] = ["Golden Ale"]

		self.food2beer["Risotto"] = ["Golden Ale"]
		self.food2beer["Sausage"] = ["English Style Bitter"]

		self.food2beer["Salad"] = ["Hefeweizen"]
		self.food2beer["Salami"] = ["Belgian-Style Tripel"]

		self.food2beer["Salmon"] = ["Brown Ale"]
		self.food2beer["Salsa"] = ["Blonde Ale"]

		self.food2beer["Sausage"] = ["Brown Ale"]
		self.food2beer["Samosas"] = ["Pale Ale"]
		self.food2beer["Scallops"] = ["Wheat Ale"]

		self.food2beer["Seafood"] = ["Hefeweizen", "Witbier"]
		self.food2beer["Shellfish"] = ["Golden Ale"]

		self.food2beer["Shrimp"] = ["Hefeweizen", "Wheat Ale"]
		self.food2beer["Smoked"] = ["Amber Ale"]
		self.food2beer["Spaghetti"] = ["Golden Ale"]

		self.food2beer["Spicy"] = ["IPA", "American IPA", "Double IPA"]
		self.food2beer["Spiced"] = ["Pale Ale"]
		self.food2beer["Suishi"] = ["American White Ale"]
		self.food2beer["Sweet"] = ["Porter", 'Stout']
		self.food2beer["Tilapia"] = ["Hefeweizen"]
		self.food2beer["Taco"] = ["Hefeweizen"]
		self.food2beer["Tomato"] = ["Lager"]

		self.food2beer["Tuna"] = ["Lager"]
		self.food2beer["Turkey"] = ["Porter", 'Stout']
		self.food2beer["Vegetable"] = ["Hefeweizen"]

		print Food.objects.all()

		print "\n\n\n"
		for food in Food.objects.all():
			print food
			beerTypeArr = self.food2beer[str(food)]
			print beerTypeArr
			for beer in Beer.objects.all():
				#print beer.beerType
				#print self.food2beer[str(food)]
				if beer.beerType  in beerTypeArr:
					food.beer.add(beer)
				else:
					pass
					#print "\t" + str(food) + " - " + str(beer)
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
		#Food.objects.filter(name="Spicy")[0].beer.all()[1].brewery

		print "Finished populating Food2Beer"

Pop()