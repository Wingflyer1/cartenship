from django.conf.urls import url
from django.views.generic import ListView

from . import views
from .models import Charterer, Port, Vessel, Chart, Voyage, Income

urlpatterns = [
    # startpage
    url(r'^$', views.home, name='home'),

    #charterer urls
    url(r'^create_charterer/$', views.create_charterer, name='create_charterer'),
    url(r'^charterer_list/$', ListView.as_view(queryset=Charterer.objects.all().order_by('company_name'), template_name="VoyageCalc/charterer_list.html"), name='charterer-list'),
    url(r'^(?P<id>[0-9]+)/edit_charterer$', views.edit_charterer, name='edit-charterer'),

    # port urls
    url(r'^create_port/$', views.create_port, name='create_port'),
    url(r'^port_list/$', ListView.as_view(queryset=Port.objects.all().order_by('port_name'), template_name="VoyageCalc/port_list.html"), name='port-list'),
    url(r'^(?P<id>[0-9]+)/edit_port$', views.edit_port, name='edit-port'),

    # vessel urls
    url(r'^create_vessel/$', views.create_vessel, name='create_vessel'),
    url(r'^vessel_list/$', ListView.as_view(queryset=Vessel.objects.all().order_by('vessel_name'), template_name="VoyageCalc/vessel_list.html"), name='vessel-list'),
    url(r'^(?P<id>[0-9]+)/edit_vessel$', views.edit_vessel, name='edit-vessel'),

    # chart urls
    url(r'^create_chart/$', views.create_chart, name='create_chart'),
    url(r'^chart_list/$', ListView.as_view(queryset=Chart.objects.filter(finished=False).order_by('-id'), template_name="VoyageCalc/chart_list.html"), name='chart-list'),
    url(r'^chart_list_finished/$', ListView.as_view(queryset=Chart.objects.filter(finished=True).order_by('-id'), template_name="VoyageCalc/chart_list_finished.html"), name='finished-charts'),
    url(r'^(?P<id>[0-9]+)/edit_chart$', views.edit_chart, name='edit-chart'),
    
    # voyage urls
    url(r'^create_voyage/$', views.create_voyage, name='create_voyage'),
    url(r'^voyage_list/$', ListView.as_view(queryset=Voyage.objects.filter(finished=False).order_by('-id'), template_name="VoyageCalc/voyage_list.html"), name='voyage-list'),
    url(r'^voyage_list_finished/$', ListView.as_view(queryset=Voyage.objects.filter(finished=True).order_by('-id'), template_name="VoyageCalc/voyage_list_finished.html"), name='finished-voyages'),
    url(r'^(?P<id>[0-9]+)/edit_voyage$', views.edit_voyage, name='edit-voyage'),

    # cost & income urls
    url(r'^(?P<id>[0-9]+)/add_income/$', views.add_income, name='add_income'),
    url(r'^(?P<id>[0-9]+)/add_cost/$', views.add_cost, name='add_cost'),
    ]