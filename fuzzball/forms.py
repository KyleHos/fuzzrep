from django import forms

class MyForm(forms.Form):
    pet_name = forms.CharField(max_length=40)
    species = forms.CharField(max_length=30)
    age = forms.IntegerField(max_value=100)
    color = forms.CharField(max_length=20)
    food_preference = forms.CharField(max_length=100)
