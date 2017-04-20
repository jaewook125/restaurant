from django import forms
from .models import Restaurant

class RestForm(forms.ModelForm):
    restname = forms.CharField(label='restname')
    class Meta:
        model = Restaurant
        fields = ('restimage','restname','restsite',)
