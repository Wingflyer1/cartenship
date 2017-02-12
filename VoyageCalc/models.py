from django.db import models
from django.contrib.auth.models import User

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
    switch_board = models.CharField(max_length=30, blank=True)
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

    # def book_summarys(self):
    #     story = self.story
    #     return story[:180]

    # def dice_result(self):
    #     count = 0
    #     sum = 0
    #     try:
    #         for comment in self.comment_set.all():
    #             count += 1
    #             sum += int(comment.dice)
    #             result = sum/float(count)
    #         return result
    #     except:
    #         return '--'

    class Meta:
        ordering = ['name']


class Vessel(models.Model):

    name = models.CharField(max_length=250)
    telephone = models.CharField(max_length=250, blank=True)
    cons_lad = models.FloatField(default=0, blank=True)
    cons_bal = models.FloatField(default=0, blank=True)
    cons_por_mgo = models.FloatField(default=0, blank=True)
    cons_por_ifo = models.FloatField(default=0, blank=True)
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
    name = models.CharField(max_length=50, blank=True)
    charterer = models.ForeignKey(Charterer, on_delete=models.CASCADE)
    ports = models.ManyToManyField(Port)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    comment = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_by", default=False, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    finished = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return "{} --> ({})".format(self.name, self.charterer)

    def __unicode__(self):
        return "{} --> ({})".format(self.name, self.charterer)

    def num_ports(self):
        return self.ports

    class Meta:
        ordering = ['name']

class Voyage(models.Model):

    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    lumpsum = models.FloatField()
    date_start = models.DateField()
    date_end = models.DateField()
    days_at_sea = models.FloatField()
    days_in_port = models.FloatField()
    port_disp = models.FloatField()
    misc_exp = models.FloatField()
    comission = models.FloatField(default=0.0)
    comment = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    finished = models.BooleanField()

    def __str__(self):  
        return '{}'.format(self.id)

    def __unicode__(self):
        return '{}'.format(self.id)

    def voyage_ports(self):
        ports = self.chart.ports       
        return ports

    def gross_freight(self):
        result = self.lumpsum-self.port_disp-self.misc_exp
        commission = result*(self.comment/100)
        return result-commission


    class Meta:
        ordering = ['-id']