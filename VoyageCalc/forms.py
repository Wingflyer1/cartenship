from django import forms
from .models import Charterer, Port, Vessel, Chart, Voyage



class ChartererCreateForm(forms.ModelForm):

    name = forms.CharField(max_length=250, label='Name')
    address = forms.CharField(max_length=250, label='Address')
    country = forms.CharField(max_length=250, label='Country')
    switch_board = forms.CharField(max_length=250, label='Phone')
    contact_person = forms.CharField(max_length=250, label='Contact Person')
    comment = forms.CharField(widget=forms.Textarea, required=False)

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

class PortCreateForm(forms.ModelForm):

    name = forms.CharField(max_length=250)
    price = forms.CharField(max_length=250)    
    contact_person = forms.CharField(max_length=250, required=False, label='Contact Person')
    telephone = forms.CharField(max_length=250, required=False)
    comment = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Port
        fields = [
            'name',
            'price',
            'contact_person',
            'telephone',          
            'comment',      
        ]

class VesselCreateForm(forms.ModelForm):

    name = forms.CharField(max_length=250, label='Vessel name')
    telephone = forms.CharField(max_length=250, required=False)
    cons_lad = forms.CharField(max_length=250, label='Consumption Laden')    
    cons_bal = forms.CharField(max_length=250, label='Consumption Ballast')
    cons_por_mgo = forms.CharField(max_length=250, label='Consumption Port MGO')
    cons_por_ifo = forms.CharField(max_length=250, label='Consumption Port IFO')
    comment = forms.CharField(widget=forms.Textarea, required=False, initial='Who is master?')

    class Meta:
        model = Vessel
        fields = [
            'name',
            'telephone',
            'cons_lad',
            'cons_bal',
            'cons_por_mgo',
            'cons_por_ifo',
            'comment',      
        ]

class ChartCreateForm(forms.ModelForm):

    name = forms.CharField(required=False)
    charterer = forms.ModelChoiceField(queryset=Charterer.objects.all(), empty_label=None)
    ports = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Port.objects.filter(deleted=False))
    date_start = forms.DateField(widget=forms.DateInput, initial='DD MM YYYY')
    date_end = forms.DateField(widget=forms.DateInput, initial='DD MM YYYY')
    comment = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Chart
        fields = [
            'name',
            'charterer',
            'date_start',
            'date_end',
            'comment',      
        ]

class VoyageCreateForm(forms.ModelForm):

    chart = forms.ModelChoiceField(queryset=Chart.objects.filter(deleted=False), empty_label=None)
    vessel = forms.ModelChoiceField(queryset=Vessel.objects.filter(deleted=False), empty_label=None)
    date_start = forms.DateField(widget=forms.DateInput, initial='DD MM YYYY')
    date_end = forms.DateField(widget=forms.DateInput, initial='DD MM YYYY')
    days_in_port = forms.CharField(required=False)
    days_at_sea = forms.CharField(required=False)
    extra_cost = forms.CharField(required=False)
    commision = forms.CharField(max_length=5, initial="%")
    comment = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:   
        model = Voyage
        fields = [
                'chart',
                'vessel',
                'date_start',
                'date_end',
                'days_in_port',
                'days_at_sea',
                'extra_cost',
                'comment',
    ]