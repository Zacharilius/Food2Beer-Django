from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect

from food2beer_app.models import Brewery, Beer, Food
from food2beer_app.forms import FoodForm

def food2beer(request):
	form = FoodForm()
	context_dict = {'nav_food2beer': 'active', 'form': form}
	if request.method == 'POST':
		recForm = FoodForm(request.POST)
		if recForm.is_valid():
			foodString = ConvertInputToBeer(request.POST.get("inputFood",""))
			foodBeerCombo = foodString.getBeerRecom();
			context_dict["foodBeerCombo"] = foodBeerCombo
	return render(request, 'food2beer_app/food2beer.html', context_dict)

class BreweryListView(ListView):
	def get_queryset(self):
		slug = self.kwargs['slug']
		try:
			brewery = Brewery.objects.get(slug=slug)
			return Beer.objects.filter(brewery=brewery)
		except Brewery.DoesNotExist:
			return Beer.objects.none()


class ConvertInputToBeer():
	def __init__(self, input):
		self.inputFoods = input.split(' ')

	def getBeerRecom(self):
		output = []
		for food in self.inputFoods:
			print food
			if (Food.objects.filter(name=food).exists()):
				matches = Food.objects.filter(name=food)[0].beer.all()
				for match in matches:
					output.append(food + " pairs with " + str(match.brewery) + " - " + str(match.name))
			else:
				output.append(food  + " isn't in the database")
		print output
		return output