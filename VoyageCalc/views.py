from django.shortcuts import render, get_object_or_404, redirect
from .models import Charterer
from .forms import ChartererCreateForm

from django.contrib.auth.models import User

app_name='VoyageCalc'


def index(request):
	title = "TC-Eq Index"
	voyages = [['0255','Glencore', '5.5', '2', '87.0', '38500', 75000], 
	           ['0256', 'Glencore', 'Carten Elina', '4.8', '1.3', '56', 65000],
	           ['0257', 'South Pacific Trade Company', '2.1', '0', '22', '25000',-18000]]

	context = {
		'title': title,
		'voyages': voyages,
	}
	return render(request, 'VoyageCalc/index.html', context)

def create_chart(request):
	voyages = ""
	return render(request, 'VoyageCalc/new_chart.html', context)

def chart_details(request):
	title = "Still under construction"

	voyages = [['', '', '', '', '', '']]

	context = {
		'title': title,
		'voyages': voyages,
	}
	return render(request, 'VoyageCalc/index.html', context)

def update_chart(request):
	context = ""
	return render(request, 'VoyageCalc/update_chart.html', context)

def delete_chart(request):
	context = ""
	return render(request, 'VoyageCalc/delete_chart.html', context)

def ship_index(request):
	title = "Ship Index"

	ship_list = [
	['Carten Maria', "https://www.google.no/maps/place/51%C2%B055'15.2%22N+4%C2%B013'55.4%22E/@51.9612793,4.0334432,9.46z/data=!4m5!3m4!1s0x0:0x0!8m2!3d51.920881!4d4.232056?hl=no", 'Rotterdam','Alta', 'Feb 20 2017', 'Read report', ['V. Putin', 'N. Krustjov'],'+47 988 75 655', False], 
	['Carten Elina', "https://www.google.no/maps/place/58%C2%B022'09.6%22N+3%C2%B047'43.0%22E/@58.6391457,0.6722019,6.42z/data=!4m5!3m4!1s0x0:0x0!8m2!3d58.369323!4d3.795265?hl=no", 'Stavanger','Edinburgh', 'Apr 20 2018', 'Read report', ['Georg Bush', 'A. Lincoln'], '+47 470 35 488', True],
	['Ness', "https://www.google.no/maps/place/62%C2%B027'12.7%22N+6%C2%B002'41.2%22E/@62.4738196,5.7610803,9.75z/data=!4m5!3m4!1s0x0:0x0!8m2!3d62.453524!4d6.044792?hl=no", 'Bergen','Kirkenes', 'May 20 2020', 'Read report', ['T. May', 'W. Churchill'], '+47 988 75 655', True]]

	context = {
		'title': title,
		'ship_list': ship_list,
	}
	return render(request, 'VoyageCalc/ship_index.html', context)

def ship_details(request):
	title = "Details - Ness"

	ship_data = ['IMO902654', '100,15', '16', '13', '12', '14', '12', '+47 988 52 555', 'http://www.scanshipping.no/enkel/resources/particulars-ness-1.pdf']

	context = {
		'title': title,
		'ship_data': ship_data
	}
	return render(request, 'VoyageCalc/ship_details.html', context)

def create_charterer(request):
    title = 'New Charterer'
    form = ChartererCreateForm(request.POST or None)
    user = request.user
    sub_btn = "Add Charterer"
    
    if not user.is_authenticated:
        return redirect('/')
    

    if form.is_valid():
        user_logged_in = request.user
        charterer = form.save(commit=False)

        # automatic set created_by
        created_by = user_logged_in
        charterer.created_by = created_by

        # insert form data to object
        name = form.cleaned_data.get('name')
        charterer.name = name
        
        address = form.cleaned_data.get('address')
        charterer.address = address

        country = form.cleaned_data.get('country')
        charterer.country = country

        switch_board = form.cleaned_data.get('switch_board')
        charterer.switch_board = switch_board

        comment = form.cleaned_data.get('comment')
        charterer.comment = comment

        charterer.save()

        return redirect("VoyageCale:index")

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
    }

    return render(request, "VoyageCalc/form.html", context)


