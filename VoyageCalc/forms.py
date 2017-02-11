from django import forms
from .models import Charterer



class ChartererCreateForm(forms.ModelForm):

    name = forms.CharField(max_length=250, label='Name')
    address = forms.CharField(max_length=250, label='Address')
    country = forms.CharField(max_length=250, label='Country')
    switch_board = forms.CharField(max_length=250, label='Phone')
    contact_person = forms.CharField(max_length=250, label='Contact Person')
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Charterer
        fields = [
            'name',
            'address',
            'country',
            'switch_board',
            'contact_person',
            'comment',            
        ]