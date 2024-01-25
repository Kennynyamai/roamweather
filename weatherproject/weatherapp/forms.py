from django import forms

class CitySearchForm(forms.Form):
    city = forms.CharField(label='Enter a city', max_length=100)