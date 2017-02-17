from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta, datetime

class Charterer(models.Model):

    company_name = models.CharField(max_length=30)
    address = models.CharField(max_length=500, blank=True)
    country = models.CharField(max_length=20, blank=True)
    contact_person = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    e_mail = models.CharField(max_length=55, blank=True)
    comment = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)     
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name

    def __unicode__(self):
        return self.company_name

    class Meta:
        ordering = ['company_name']

class Port(models.Model):

    port_name = models.CharField(max_length=250)
    contact_person = models.CharField(max_length=250, blank=True)
    telephone = models.CharField(max_length=250, blank=True)
    e_mail = models.CharField(max_length=55, blank=True)
    comment = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)     
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.port_name

    def __unicode__(self):
        return self.port_name

    class Meta:

        ordering = ['port_name']

class Vessel(models.Model):

    vessel_name = models.CharField(max_length=250)
    telephone = models.CharField(max_length=250, blank=True)
    bunker_price_mgo = models.FloatField(default=0, blank=False)
    bunker_price_ifo = models.FloatField(default=0, blank=False)

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
        return self.vessel_name

    def __unicode__(self):
        return self.vessel_name

    class Meta:
        ordering = ['vessel_name']

class Chart(models.Model):
    chart_name = models.CharField(max_length=150, blank=True)
    charterer = models.ForeignKey(Charterer, on_delete=models.CASCADE, related_name="chart_charterer")
    ports = models.ManyToManyField(Port)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    comment = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_by", default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

    def __str__(self):
        charterer = str(self.charterer)
        return "{}... -> {}".format(charterer[:10], self.chart_name.strip(" "))

    def __unicode__(self):
        charterer = str(self.charterer)
        return "{}... -> {}".format(charterer[:10], self.chart_name.strip(" "))

    class Meta:
        ordering = ['id']

    def chart_number(self):
        result = str(self.id).zfill(4)
        return result

    def number_of_voyages(self):
        voyages = self.voyage_set.all()
        result = len(voyages)
        return result

    def avg_tc(self):
        all_chart_voyages = Voyage.objects.filter(chart=self)
        total_tc = 0
        num_voyages = int(len(all_chart_voyages))
        print(num_voyages)
        for voyage in all_chart_voyages:
            voy_tc = float(voyage.tc_equiv())
            print(voy_tc)
            total_tc += voy_tc
        return total_tc/num_voyages



class Voyage(models.Model):
    # relations
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    # duration
    date_start = models.DateField()
    date_end = models.DateField()
    # bunkers
    days_at_sea_laden = models.FloatField(blank=True, default=0)
    days_at_sea_ballast = models.FloatField(blank=True, default=0)
    days_in_port_mgo = models.FloatField(blank=True, default=0)
    days_in_port_ifo = models.FloatField(blank=True, default=0)
    # expenses
    commission_p = models.FloatField(blank=False, default=0)
    # meta
    comment = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voy_created_by")
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voy_updated_by", null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    finished = models.BooleanField()

    class Meta:
        ordering = ['-chart']

    def __str__(self):
        return '{}'.format(self.id)

    def __unicode__(self):
        return '{}'.format(self.id)

    def voyage_number(self):
        return str(self.id).zfill(4)

    def bunkers(self):
        vessel = Vessel.objects.get(vessel_name=self.vessel)
        used_MGO = vessel.cons_bal*self.days_at_sea_ballast+vessel.cons_lad*self.days_at_sea_laden+vessel.cons_por_ifo*self.days_in_port_mgo
        used_IFO = vessel.cons_por_ifo*self.days_in_port_ifo
        result = used_IFO*vessel.bunker_price_ifo+used_MGO*vessel.bunker_price_mgo
        return float(result)

    def commission(self):
        comm = self.commission_p
        voy_inc = int(self.voyage_incomes())
        result = (comm/100) * voy_inc
        return float(result)

    def voyage_costs(self):
        costs = Cost.objects.filter(voyage=self)
        costs_sum = self.commission() + self.bunkers()
        for cost in costs:
            costs_sum += cost.cost_amount
        return costs_sum

    def voyage_incomes(self):# gross freight
        incomes = Income.objects.filter(voyage=self)
        incomes_sum = 0
        for income in incomes:
            incomes_sum += int(income.income_amount)
        return incomes_sum

    def net_freight(self):
        cost = float(self.voyage_incomes())
        comm = float(self.commission())
        bunk = float(self.bunkers())
        return cost - comm - bunk

    def color_net(self):
        if self.net_freight() > 0:
            result = "green"
        else:
            result = "red"
        return result

    def total_days(self):
        return str(self.days_in_port_ifo + self.days_in_port_mgo + self.days_at_sea_laden + self.days_at_sea_ballast)

    def tc_equiv(self):
        net_f = float(self.net_freight())
        days = float(self.total_days())
        tc_eq = net_f/days 
        return "{}".format(round(tc_eq,2))

    def chart_avg_tc(self):
        chart_voy = Voyage.objects.filter(chart = self.chart)
        result = 0
        num = len(chart_voy)
        for voy in chart_voy:
            voy_tc = float(voy.tc_equiv())
            result += voy_tc/num
        return result
        # return result


class Income(models.Model):

    income_type = models.CharField(max_length=15)
    income_amount = models.FloatField(blank=False, default=0)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    # income_reference = CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{}'.format(self.id)

    def __unicode__(self):
        return '{}'.format(self.id)

class Cost(models.Model):

    cost_type = models.CharField(max_length=15)
    cost_amount = models.FloatField(blank=False, default=0)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    # income_reference = CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)

    def __str__(self):
        return '{}'.format(self.id)

    def __unicode__(self):
        return '{}'.format(self.id)

    class Meta:
        ordering = ['-id']