from django.db import models
from django.contrib.auth.models import User

class Port(models.Model):

    name = models.CharField(max_length=250)
    price = models.CharField(max_length=10, default=0, blank=True)
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
    # length = models.CharField(max_length=10)
    # breadth = models.CharField(max_length=10)
    cons_lad = models.CharField(max_length=10, default=0)
    cons_bal = models.CharField(max_length=10, default=0)
    cons_por_mgo = models.CharField(max_length=10, default=0)
    cons_por_ifo = models.CharField(max_length=10, blank=True)
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
    chart_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    charterer = models.ForeignKey(Charterer, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    comment = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="updated_by", default=False, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.chart_number)

    def __unicode__(self):
        return str(self.chart_number)

    class Meta:
        ordering = ['-chart_number']

class Voyage(models.Model):

    voyage_number = models.AutoField(primary_key=True)
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
    days_at_sea = models.CharField(max_length=15, blank=True, default=0)
    days_in_port = models.CharField(max_length=15, blank=True, default=0)
    extra_cost = models.CharField(max_length=20, blank=True, default=0)
    comission = models.CharField(max_length=5, blank=True, default=0)
    # comment = models.TextField(default="")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voyage_updated_by")
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.voyage_number

    def __unicode__(self):
        return self.voyage_number

    class Meta:
        ordering = ['-voyage_number']