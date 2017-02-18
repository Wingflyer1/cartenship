from django.shortcuts import render, get_object_or_404, redirect
from .models import Charterer, Port, Vessel, Chart, Voyage, Income, Cost
from .forms import ChartererCreateForm, PortCreateForm, VesselCreateForm, ChartCreateForm, ChartEditForm, VoyageCreateForm, IncomeForm, CostForm
import random
from django.contrib.auth.models import User
from carten import settings
from django.utils.http import is_safe_url

app_name='VoyageCalc'


def home(request):
    title = "C-Calc"
    version = settings.VERSION

    pic_num = random.randrange(1, 4)

    user = request.user
    if not user.is_authenticated:
       return redirect('auth_login')
    context = {
        'title': title,
        'pic_num': pic_num,
        'version': version, 
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
        company_name = form.cleaned_data.get('company_name')
        split_name = company_name.split(" ")
        company_name = ""
        for i in split_name:
            company_name += (i.capitalize()) + " "
        charterer.company_name = company_name
        
        contact_person = form.cleaned_data.get('contact_person')
        charterer.contact_person = contact_person

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
        company_name = form.cleaned_data.get('company_name')
        split_name = company_name.split(" ")
        company_name = ""
        for i in split_name:
            company_name += (i.capitalize()) + " "
        charterer.company_name = company_name

        contact_person = form.cleaned_data.get('contact_person')
        charterer.contact_person = contact_person
        
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
        port_name = form.cleaned_data.get('port_name')
        split_name = port_name.split(" ")
        port_name = ""
        for i in split_name:
            port_name += (i.capitalize()) + " "
        port.port_name = port_name
        
        price = form.cleaned_data.get('price')
        port.price = price

        try:
            contact_person = form.cleaned_data.get('contact_person')
            split_name = contact_person.split(" ")
            contact_person = ""
            for i in contact_person:
                contact_person += (i.capitalize()) + " "
            port.contact_person = contact_person
        except AttributeError:
            pass


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
        port_name = form.cleaned_data.get('port_name')
        split_name = port_name.split(" ")
        port_name = ""
        for i in split_name:
            port_name += (i.capitalize()) + " "
        port.port_name = port_name
        
        price = form.cleaned_data.get('price')
        port.price = price

        try:
            contact_person = form.cleaned_data.get('contact_person')
            split_name = contact_person.split(" ")
            contact_person = ""
            for i in contact_person:
                contact_person += (i.capitalize()) + " "
            port.contact_person = contact_person
        except AttributeError:
            pass

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
        vessel_name = form.cleaned_data.get('vessel_name')
        split_name = vessel_name.split(" ")
        vessel_name = ""
        for i in split_name:
            vessel_name += (i.capitalize()) + " "
        vessel.vessel_name = vessel_name

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
        vessel_name = form.cleaned_data.get('vessel_name')
        split_name = vessel_name.split(" ")
        vessel_name = ""
        for i in split_name:
            vessel_name += (i.capitalize()) + " "
        vessel.vessel_name = vessel_name

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

        chart_name = form.cleaned_data.get('chart_name')
        chart.chart_name = chart_name

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
    form = ChartEditForm(request.POST or None, instance=chart)
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

        chart_name = form.cleaned_data.get('chart_name')
        chart.chart_name = chart_name

        ports = form.cleaned_data.get('ports')
        chart.ports = ports
        
        date_start = form.cleaned_data.get('date_start')
        chart.date_start = date_start

        date_end = form.cleaned_data.get('date_end')
        chart.date_end = date_end

        comment = form.cleaned_data.get('comment')
        chart.comment = comment

        finished = form.cleaned_data.get('finished')
        chart.finished = finished

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
    sub_btn = "Add Voyage"
    # form preparations
    form = VoyageCreateForm(request.POST or None)
    user = request.user
    
    if not user.is_authenticated:
        return redirect('/')
    

    if form.is_valid():
        user_logged_in = request.user
        voyage = form.save(commit=False)

        chart = form.cleaned_data.get('chart')
        voyage.chart = chart

        vessel = form.cleaned_data.get('vessel')
        voyage.vessel = vessel
        
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

        commission_p = form.cleaned_data.get('commission_p')
        voyage.commission_p = commission_p
        
        comment = form.cleaned_data.get('comment')
        voyage.comment = comment

        created_by = user_logged_in
        voyage.created_by = created_by

        voyage.save()

        return redirect("VoyageCalc:edit-voyage", voyage)

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
    }

    return render(request, "VoyageCalc/form.html", context)

def edit_voyage(request, id=None):
    title = 'Edit Voyage'
    voyage = Voyage.objects.get(id=id)
    income_form = IncomeForm(request.POST or None)
    form = VoyageCreateForm(request.POST or None, instance=voyage)
    incomes = Income.objects.filter(voyage = voyage)
    costs = Cost.objects.filter(voyage = voyage)
    chart = Chart.objects.get(id = id)

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

        commission_p = form.cleaned_data.get('commission_p')
        voyage.commission_p = commission_p

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
        'incomes': incomes,
        'voyage': voyage,
        'costs': costs,
        'chart': chart,
    }

    return render(request, "VoyageCalc/voyage_form.html", context)

def add_income(request, id=None):
    title = 'New Income'
    sub_btn = "Add Income"
    form = IncomeForm(request.POST or None)
    user = request.user
    voyage = Voyage.objects.get(id=id)
    
    # get url of voyage-page
    came_from_page = request.GET.get('from', None)
    print(came_from_page)
    
    if not user.is_authenticated:
        return redirect('/')
    
    if form.is_valid():
        user_logged_in = request.user
        income = form.save(commit=False)

        # automatic set created_by
        created_by = user_logged_in
        income.created_by = created_by
      
        income_type = form.cleaned_data.get('income_type')
        income.income_type = income_type

        income.voyage = voyage

        income_amount = form.cleaned_data.get('income_amount')
        income.income_amount = income_amount

        income.save()

        next = request.GET.get('next', None)
        if next:
            return redirect(next)

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
        'came_from_page': came_from_page
    }

    return render(request, "VoyageCalc/form.html", context)

def add_cost(request, id=None):
    title = 'New Cost'
    sub_btn = "Add Cost"
    form = CostForm(request.POST or None)
    user = request.user
    voyage = Voyage.objects.get(id=id)
    currencies = [('USD', 0.12),
                    ('EUR', 0.11),
                    ('SEK', 1.07),
                    ('DKK', 0.84),]
    
    # get url of voyage-page
    came_from_page = request.GET.get('from', None)
    print(came_from_page)
    
    if not user.is_authenticated:
        return redirect('/')
    
    if form.is_valid():
        user_logged_in = request.user
        cost = form.save(commit=False)

        # automatic set created_by
        created_by = user_logged_in
        cost.created_by = created_by
      
        cost_type = form.cleaned_data.get('cost_type')
        cost.income_type = cost_type

        cost.voyage = voyage

        cost_amount = form.cleaned_data.get('cost_amount')
        cost.income_amount = cost_amount

        cost.save()

        next = request.GET.get('next', None)
        if next:
            return redirect(next)

    context = {
        'form': form,
        'title': title,
        'sub_btn': sub_btn,
        'came_from_page': came_from_page,
        'currencies': currencies,
    }

    return render(request, "VoyageCalc/form.html", context)

# edit_cost

# edit_income