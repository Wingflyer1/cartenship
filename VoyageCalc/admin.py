from django.contrib import admin

from .models import Charterer, Chart, Port, Vessel, Voyage
# Register your models here.

admin.site.register(Charterer)

admin.site.register(Chart)

admin.site.register(Port)

admin.site.register(Vessel)

admin.site.register(Voyage)
