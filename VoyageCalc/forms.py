from django import forms
from .models import Charterer, Port, Vessel, Chart, Voyage



class ChartererCreateForm(forms.ModelForm):

    name = forms.CharField(max_length=250, label='Name', initial='Company Name')
    address = forms.CharField(max_length=250, label='Address', required=False)
    country = forms.CharField(max_length=250, label='Country', required=False)
    switch_board = forms.CharField(max_length=250, label='Phone', required=False)
    contact_person = forms.CharField(max_length=250, label='Contact Person', required=False)
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

    name = forms.CharField(max_length=250, initial="Port name")
    price = forms.FloatField()
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
    cons_lad = forms.FloatField(label='Consumption Laden')    
    cons_bal = forms.FloatField(label='Consumption Ballast')
    cons_por_mgo = forms.FloatField(label='Consumption Port MGO')
    cons_por_ifo = forms.FloatField(label='Consumption Port IFO')
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

    name = forms.CharField(max_length=150, required=True)
    charterer = forms.ModelChoiceField(queryset=Charterer.objects.all(), empty_label=None)
    ports = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Port.objects.filter(deleted=False))
    date_start = forms.DateField(widget=forms.DateInput, initial='ie. 12 apr 1977')
    date_end = forms.DateField(widget=forms.DateInput, initial='ie. 12 apr 1977')
    comment = forms.CharField(widget=forms.Textarea, required=False)
    finished = forms.BooleanField(required=False)


    class Meta:
        model = Chart
        fields = [
            'name',
            'charterer',
            'ports',
            'date_start',
            'date_end',
            'comment',
            'finished',
        ]

class VoyageCreateForm(forms.ModelForm):

    chart = forms.ModelChoiceField(queryset=Chart.objects.all(), empty_label=None)
    vessel = forms.ModelChoiceField(queryset=Vessel.objects.all(), empty_label=None)
    lumpsum = forms.FloatField()
    date_start = forms.DateField(widget=forms.DateInput, initial='ie. 12 apr 1977')
    date_end = forms.DateField(widget=forms.DateInput, initial='ie. 12 apr 1977')
    days_in_port = forms.CharField(required=False)
    days_at_sea = forms.CharField(required=False)
    port_disp = forms.FloatField(label="Port dispursement")
    misc_exp = forms.FloatField(label="Misc expenses")
    commission = forms.FloatField(help_text="ie. 2.5")
    comment = forms.CharField(widget=forms.Textarea, required=False)
    finished = forms.BooleanField(required=False)

    class Meta:   
        model = Voyage
        fields = [
                'chart',
                'vessel',
                'lumpsum',
                'date_start',
                'date_end',
                'days_at_sea',
                'days_in_port',
                'port_disp',
                'misc_exp',
                'commission',
                'comment',
                'finished',
    ]