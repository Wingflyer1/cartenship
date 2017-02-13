from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta

class Port(models.Model):

    name = models.CharField(max_length=250)
    price = models.FloatField(default=0)
    contact_person = models.CharField(max_length=250, blank=True)
    telephone = models.CharField(max_length=250, blank=True)
    comment = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)     
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:

        ordering = ['name']

class Charterer(models.Model):

    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500, blank=True)
    country = models.CharField(max_length=20, blank=True)
    switch_board = models.CharField(max_length=50, blank=True)
    contact_person = models.CharField(max_length=100, blank=True)
    comment = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)     
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Vessel(models.Model):

    name = models.CharField(max_length=250)
    telephone = models.CharField(max_length=250)
    bunker_price_mgo = models.FloatField(default=0)
    bunker_price_ifo = models.FloatField(default=0)

    cons_lad = models.FloatField(default=0)
    cons_bal = models.FloatField(default=0)
    cons_por_mgo = models.FloatField(default=0)
    cons_por_ifo = models.FloatField(default=0)

    comment = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)     
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Chart(models.Model):
    name = models.CharField(max_length=150, blank=True)
    charterer = models.ForeignKey(Charterer, on_delete=models.CASCADE, related_name="chart_charterer")
    ports = models.ManyToManyField(Port)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    comment = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_by", default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    finished = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def chart_number(self):
        result = str(self.id).zfill(4)
        return result

    def number_of_voyages(self):
        voyages = self.voyage_set.all()
        result = len(voyages)
        return result        

class Voyage(models.Model):
    # relations
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    # income
    lumpsum = models.FloatField()
    other_inc = models.FloatField()
    # duration
    date_start = models.DateField()
    date_end = models.DateField()
    # bunkers
    days_at_sea_laden = models.FloatField(blank=True, default=0)
    days_at_sea_ballast = models.FloatField(blank=True, default=0)
    days_in_port_mgo = models.FloatField(blank=True, default=0)
    days_in_port_ifo = models.FloatField(blank=True, default=0)
    # expenses
    port_disp = models.FloatField()
    misc_exp = models.FloatField()
    commission = models.FloatField()

    comment = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voy_created_by")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voy_updated_by", null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    finished = models.BooleanField()

    def __str__(self):
        return '{}'.format(self.id)

    def __unicode__(self):
        return '{}'.format(self.id)

    def voyage_number(self):
        result = str(self.id).zfill(4)
        return result

    class Meta:
        ordering = ['-chart']

    def ports(self):
        result = self.chart.ports.all()
        return result

    def duration(self):
        d0 = self.date_start
        d1 = self.date_end
        delta = d1-d0
        tdelta = delta.days
        return float(tdelta)

    def over_chart(self):
        avg = int(self.avg_tc())
        own_tc = int(self.tc_eq())
        if own_tc>=avg*1.25:
            print('jopp')
            return True
        else:
            print('neipp')
            return False

    def gross_freight(self):
        return self.lumpsum + self.other_inc

    def commission_(self):
        print('here now')
        gross_freight = self.gross_freight()
        com = self.commission
        try:
            result = (com/100)*gross_freight
        except:
            print('failure')
            result = 0
        return result

    def bunkers(self):
        sea_lad = self.vessel.cons_lad*self.days_at_sea_laden
        sea_bal = self.vessel.cons_bal*self.days_at_sea_ballast
        port_mgo = self.vessel.cons_por_mgo*self.days_in_port_mgo
        port_ifo = self.vessel.cons_por_ifo*self.days_in_port_ifo
        result = sea_lad + sea_bal + port_mgo + port_ifo
        return result

    def total_exp(self):
        result = self.bunkers()+self.commission+self.port_disp+self.misc_exp
        return result

    def net_freight(self):
        return float(self.gross_freight()-self.total_exp())

    def tc_eq(self):
        duration = self.duration()
        return float(self.net_freight()/duration)

    def avg_tc(self):
        object_list = Voyage.objects.filter(chart=self.chart)
        tc_sum = 0
        num = 0
        for object_ in object_list:
            tc = int(object_.tc_eq())
            print(tc)
            num += 1
            tc_sum += tc
        result = tc_sum/num
        print(tc_sum, num, 'blir dette riktig da?')
        print(result)
        return result

