from django import forms

#The form in the searchbar
class CitySearchForm(forms.Form):
    city = forms.CharField(label='Enter a city', max_length=100)