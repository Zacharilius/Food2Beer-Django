from django import forms

class FoodForm(forms.Form):
	inputFood = forms.CharField(label='Input Food', max_length=100, initial="Spicy Chinese")