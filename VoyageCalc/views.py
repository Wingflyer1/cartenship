from django.shortcuts import render, get_object_or_404, redirect
from .models import Charterer, Port, Vessel, Chart, Voyage
from .forms import ChartererCreateForm, PortCreateForm, VesselCreateForm, ChartCreateForm, VoyageCreateForm 

from django.contrib.auth.models import User

app_name='VoyageCalc'


def home(request):
	title = "C-Calc"
	voyages = [['0255','Glencore', '5.5', '2', '87.0', '38500', 75000], 
	           ['0256', 'Glencore', 'Carten Elina', '4.8', '1.3', '56', 65000],
	           ['0257', 'South Pacific Trade Company', '2.1', '0', '22', '25000',-18000]]
	user = request.user
	if not user.is_authenticated:
		return redirect('auth_login')		
	context = {
		'title': title,
		'voyages': voyages,
	}
	return render(request, 'VoyageCalc/home.html', context)

# Charterer views
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
        split_name = name.split(" ")
        name = ""
        for i in split_name:
            name += (i.capitalize()) + " "
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

        return redirect("VoyageCalc:charterer-list")

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
    }

    return render(request, "VoyageCalc/form.html", context)

def edit_charterer(request, id=None):
    title = 'Update Charterer'
    charterer = Charterer.objects.get(id=id)
    form = ChartererCreateForm(request.POST or None, instance=charterer)
    user = request.user
    sub_btn = "Update"
    
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
        split_name = name.split(" ")
        name = ""
        for i in split_name:
            name += (i.capitalize()) + " "
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

        return redirect("VoyageCalc:charterer-list")

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
    }

    return render(request, "VoyageCalc/form.html", context)

# port views
def create_port(request):
    title = 'New Port'
    form = PortCreateForm(request.POST or None)
    user = request.user
    sub_btn = "Add Port"
    
    if not user.is_authenticated:
        return redirect('/')
    

    if form.is_valid():
        user_logged_in = request.user
        port = form.save(commit=False)

        # automatic set created_by
        created_by = user_logged_in
        port.created_by = created_by

        # insert form data to object
        name = form.cleaned_data.get('name')
        split_name = name.split(" ")
        name = ""
        for i in split_name:
            name += (i.capitalize()) + " "
        charterer.name = name
        
        price = form.cleaned_data.get('price')
        port.price = price

        contact_person = form.cleaned_data.get('contact_person')
        split_name = contact_person.split(" ")
        contact_person = ""
        for i in contact_person:
            contact_person += (i.capitalize()) + " "
        port.contact_person = contact_person

        telephone = form.cleaned_data.get('telephone')
        port.telephone = telephone

        comment = form.cleaned_data.get('comment')
        port.comment = comment

        port.save()

        return redirect("VoyageCalc:port-list")

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
    }

    return render(request, "VoyageCalc/form.html", context)

def edit_port(request, id=None):
    user = request.user
    if not user.is_authenticated:
        return redirect('/')

    title = 'Update Port'
    sub_btn = "Update"
    port = Port.objects.get(id=id)
    form = PortCreateForm(request.POST or None, instance=port)
    

    if form.is_valid():
        port = form.save(commit=False)

        # automatic set created_by
        created_by = user
        port.created_by = created_by

        # insert form data to object
        name = form.cleaned_data.get('name')
        split_name = name.split(" ")
        name = ""
        for i in split_name:
            name += (i.capitalize()) + " "
        charterer.name = name
        
        price = form.cleaned_data.get('price')
        port.price = price

        contact_person = form.cleaned_data.get('contact_person')
        split_name = contact_person.split(" ")
        contact_person = ""
        for i in contact_person:
            contact_person += (i.capitalize()) + " "
        port.contact_person = contact_person

        telephone = form.cleaned_data.get('telephone')
        port.telephone = telephone

        comment = form.cleaned_data.get('comment')
        port.comment = comment

        port.save()

        return redirect("VoyageCalc:port-list")

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
    }

    return render(request, "VoyageCalc/form.html", context)

# vessel views
def create_vessel(request):
    title = 'New Vessel'
    form = VesselCreateForm(request.POST or None)
    user = request.user
    sub_btn = "Add Vessel"
    
    if not user.is_authenticated:
        return redirect('/')
    

    if form.is_valid():
        user_logged_in = request.user
        vessel = form.save(commit=False)

        # automatic set created_by
        created_by = user_logged_in
        vessel.created_by = created_by

        # insert form data to object
        name = form.cleaned_data.get('name')
        split_name = name.split(" ")
        name = ""
        for i in split_name:
            name += (i.capitalize()) + " "
        charterer.name = name

        telephone = form.cleaned_data.get('telephone')
        vessel.telephone = telephone
        
        cons_lad = form.cleaned_data.get('cons_lad')
        vessel.cons_lad = cons_lad

        cons_bal = form.cleaned_data.get('cons_bal')
        vessel.cons_bal = cons_bal

        cons_por_mgo = form.cleaned_data.get('cons_por_mgo')
        vessel.cons_por_mgo = cons_por_mgo

        cons_por_ifo = form.cleaned_data.get('cons_por_ifo')
        vessel.cons_por_ifo = cons_por_ifo

        comment = form.cleaned_data.get('comment')
        vessel.comment = comment

        vessel.save()

        return redirect("VoyageCalc:vessel-list")

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
    }

    return render(request, "VoyageCalc/form.html", context)

def edit_vessel(request, id=None):
    title = 'Update Vessel'
    vessel = Vessel.objects.get(id=id)
    form = VesselCreateForm(request.POST or None, instance=vessel)
    user = request.user
    sub_btn = "Update"
    
    if not user.is_authenticated:
        return redirect('/')
    

    if form.is_valid():
        user_logged_in = request.user
        vessel = form.save(commit=False)

        # automatic set created_by
        created_by = user_logged_in
        vessel.created_by = created_by

        # insert form data to object
        name = form.cleaned_data.get('name')
        split_name = name.split(" ")
        name = ""
        for i in split_name:
            name += (i.capitalize()) + " "
        charterer.name = name

        telephone = form.cleaned_data.get('telephone')
        vessel.telephone = telephone
        
        cons_lad = form.cleaned_data.get('cons_lad')
        vessel.cons_lad = cons_lad

        cons_bal = form.cleaned_data.get('cons_bal')
        vessel.cons_bal = cons_bal

        cons_por_mgo = form.cleaned_data.get('cons_por_mgo')
        vessel.cons_por_mgo = cons_por_mgo

        cons_por_ifo = form.cleaned_data.get('cons_por_ifo')
        vessel.cons_por_ifo = cons_por_ifo

        comment = form.cleaned_data.get('comment')
        vessel.comment = comment

        vessel.save()

        return redirect("VoyageCalc:vessel-list")

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
    }

    return render(request, "VoyageCalc/form.html", context)

# chart views
def create_chart(request):
    title = 'New Chart'
    form = ChartCreateForm(request.POST or None)
    user = request.user
    sub_btn = "Add Chart"
    
    if not user.is_authenticated:
        return redirect('/')
    

    if form.is_valid():
        user_logged_in = request.user
        chart = form.save(commit=False)

        created_by = user_logged_in
        chart.created_by = created_by

        name = form.cleaned_data.get('name')
        split_name = name.split(" ")
        name = ""
        for i in split_name:
            name += (i.capitalize()) + " "
        charterer.name = name

        charterer = form.cleaned_data.get('charterer')
        chart.charterer = charterer

        ports = form.cleaned_data.get('ports')
        
        date_start = form.cleaned_data.get('date_start')
        chart.date_start = date_start

        date_end = form.cleaned_data.get('date_end')
        chart.date_end = date_end

        comment = form.cleaned_data.get('comment')
        chart.comment = comment

        chart.save()
        chart.ports = ports
        chart.save()

        return redirect("VoyageCalc:chart-list")

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
    }

    return render(request, "VoyageCalc/form.html", context)

def edit_chart(request, id=None):
    title = 'Update Chart'
    chart = Chart.objects.get(id=id)
    form = ChartCreateForm(request.POST or None, instance=chart)
    user = request.user
    sub_btn = "Update"
    
    if not user.is_authenticated:
        return redirect('/')
    

    if form.is_valid():
        user_logged_in = request.user
        chart = form.save(commit=False)

        # automatic set created_by
        updated_by = user_logged_in
        chart.updated_by = updated_by

        charterer = form.cleaned_data.get('charterer')
        chart.charterer = charterer

        ports = form.cleaned_data.get('ports')
        chart.ports = ports
        
        date_start = form.cleaned_data.get('date_start')
        chart.date_start = date_start

        date_end = form.cleaned_data.get('date_end')
        chart.date_end = date_end

        comment = form.cleaned_data.get('comment')
        chart.comment = comment

        name = form.cleaned_data.get('name')
        split_name = name.split(" ")
        name = ""
        for i in split_name:
            name += (i.capitalize()) + " "
        charterer.name = name

        chart.save()

        return redirect("VoyageCalc:chart-list")

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
    }

    return render(request, "VoyageCalc/form.html", context)

# voyage views
def create_voyage(request):
    title = 'New Voyage'
    form = VoyageCreateForm(request.POST or None)
    user = request.user
    sub_btn = "Add Voyage"
    
    if not user.is_authenticated:
        return redirect('/')
    

    if form.is_valid():
        user_logged_in = request.user
        voyage = form.save(commit=False)

        chart = form.cleaned_data.get('chart')
        voyage.chart = chart

        vessel = form.cleaned_data.get('vessel')
        voyage.vessel = vessel
        
        lumpsum = form.cleaned_data.get('lumpsum')
        voyage.lumpsum = lumpsum

        other_inc = form.cleaned_data.get('other_inc')
        voyage.other_inc = other_inc

        date_start = form.cleaned_data.get('date_start')
        voyage.date_start = date_start

        date_end = form.cleaned_data.get('date_end')
        voyage.date_end = date_end

        days_at_sea_laden = form.cleaned_data.get('days_at_sea_laden')
        voyage.days_at_sea_laden = days_at_sea_laden

        days_at_sea_ballast = form.cleaned_data.get('days_at_sea_ballast')
        voyage.days_at_sea_ballast = days_at_sea_ballast

        days_in_port_mgo = form.cleaned_data.get('days_in_port_mgo')
        voyage.days_in_port_mgo = days_in_port_mgo

        days_in_port_ifo = form.cleaned_data.get('days_in_port_ifo')
        voyage.days_in_port_ifo = days_in_port_ifo

        port_disp = form.cleaned_data.get('port_disp')
        voyage.port_disp = port_disp

        misc_exp = form.cleaned_data.get('misc_exp')
        voyage.misc_exp = misc_exp

        commission = form.cleaned_data.get('commission')
        voyage.commission = commission
        
        comment = form.cleaned_data.get('comment')
        voyage.comment = comment

        created_by = user_logged_in
        voyage.created_by = created_by

        voyage.save()

        return redirect("VoyageCalc:voyage-list")

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
    }

    return render(request, "VoyageCalc/form.html", context)

def edit_voyage(request, id=None):
    title = 'Edit Voyage'
    voyage = Voyage.objects.get(id=id)
    form = VoyageCreateForm(request.POST or None, instance=voyage)
    user = request.user
    sub_btn = "Save changes"
    
    if not user.is_authenticated:
        return redirect('/')
    

    if form.is_valid():
        user_logged_in = request.user
        voyage = form.save(commit=False)

        updated_by = user_logged_in
        voyage.updated_by = updated_by

        chart = form.cleaned_data.get('chart')
        voyage.chart = chart

        vessel = form.cleaned_data.get('vessel')
        voyage.vessel = vessel
        
        lumpsum = form.cleaned_data.get('lumpsum')
        voyage.lumpsum = lumpsum

        other_inc = form.cleaned_data.get('other_inc')
        voyage.other_inc = other_inc

        date_start = form.cleaned_data.get('date_start')
        voyage.date_start = date_start

        date_end = form.cleaned_data.get('date_end')
        voyage.date_end = date_end

        days_at_sea_laden = form.cleaned_data.get('days_at_sea_laden')
        voyage.days_at_sea_laden = days_at_sea_laden

        days_at_sea_ballast = form.cleaned_data.get('days_at_sea_ballast')
        voyage.days_at_sea_ballast = days_at_sea_ballast

        days_in_port_mgo = form.cleaned_data.get('days_in_port_mgo')
        voyage.days_in_port_mgo = days_in_port_mgo

        days_in_port_ifo = form.cleaned_data.get('days_in_port_ifo')
        voyage.days_in_port_ifo = days_in_port_ifo

        port_disp = form.cleaned_data.get('port_disp')
        voyage.port_disp = port_disp

        misc_exp = form.cleaned_data.get('misc_exp')
        voyage.misc_exp = misc_exp

        commission = form.cleaned_data.get('commission')
        voyage.commission = commission

        updated_by = user_logged_in
        voyage.updated_by = updated_by
        
        comment = form.cleaned_data.get('comment')
        voyage.comment = comment

        finished = form.cleaned_data.get('finished')
        voyage.finished = finished

        voyage.save()

        return redirect("VoyageCalc:voyage-list")

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
    }

    return render(request, "VoyageCalc/form.html", context)