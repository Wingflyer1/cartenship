from django import forms
from .models import Charterer, Port, Vessel, Chart, Voyage, Income, Cost
from datetime import date

class ChartererCreateForm(forms.ModelForm):

    class Meta:
        model = Charterer
        exclude = [
                'created_by',
                'created',
                'updated',
                'deleted',
        ]

class PortCreateForm(forms.ModelForm):

    class Meta:
        model = Port
        exclude = [
                'created_by',
                'created',
                'updated',
                'deleted',
        ]

class VesselCreateForm(forms.ModelForm):

    cons_lad = forms.FloatField(label='Consumption Laden')
    cons_bal = forms.FloatField(label='Consumption Ballast')
    cons_por_mgo = forms.FloatField(label='Consumption Port MGO')
    cons_por_ifo = forms.FloatField(label='Consumption Port IFO')

    class Meta:
        model = Vessel
        exclude = [
                   'created',
                   'created_by',
                   'updated',
                   'deleted',
        ]

class ChartCreateForm(forms.ModelForm):

    date_start = forms.DateField(widget=forms.DateInput, initial='ie. 12 apr 1977')
    date_end = forms.DateField(widget=forms.DateInput, initial='ie. 12 apr 1977')
    
    class Meta:
        model = Chart
        exclude = [
                'created_by',
                'updated_by',
                'finished',
                'created',
                'updated',
                'deleted',
        ]

class VoyageCreateForm(forms.ModelForm):

    chart = forms.ModelChoiceField(queryset=Chart.objects.all(), empty_label=None)
    vessel = forms.ModelChoiceField(queryset=Vessel.objects.all(), empty_label=None)

    date_start = forms.DateField()
    date_end = forms.DateField()

    comment = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:   
        model = Voyage
        exclude = [
                'created_by',
                'created',
                'updated_by',
                'updated',
    ]

class IncomeForm(forms.ModelForm):

    INCOME_TYPES = (
                ('LS','Freight Lumpsum'),
                ('TFI', 'Total Freight Income'),
                ('OFI','Other Freight Incomes'),
                ('DD', 'Demurrage/Despatch'),
        )

    income_type = forms.ChoiceField(choices=INCOME_TYPES)

    class Meta:   
        model = Income
        exclude = [
                    'created_by',
                    'created',
                    'updated',
                    'voyage',
        ]

class CostForm(forms.ModelForm):
    COST_TYPES = (
                ('PD','Port Dispursement'),
                ('ME','Misc. Expenses'),
                ('BU', '* Bunkers *'),
                ('CO', '* Commission *')
        )

    cost_type = forms.ChoiceField(choices=COST_TYPES)

    class Meta:   
        model = Cost
        exclude = [
                    'created_by',
                    'created',
                    'updated',
                    'voyage',
        ]