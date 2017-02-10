from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Chart(models.Model):

#     chartnumber = models.CharField(max_length=250)
#     voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment = models.TextField()
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     deleted = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title

#     def __unicode__(self):
#         return self.title


#     class Meta:
#         ordering = ['-chartnumber']



# class Voyage(models.Model):

#     voyage_number = models.CharField(max_length=6)
#     from_port = models.ForeignKey(Port, on_delete=models.CASCADE)
#     to_port = models.ForeignKey(Port, on_delete=models.CASCADE)
#     charterer = models.ForeignKey(Port, on_delete=models.CASCADE)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment = models.TextField()
#     readings = models.IntegerField(default=0)
#     likes = models.IntegerField(default=0)
#     published = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     draft = models.BooleanField(default=False)
#     deleted = models.BooleanField(default=False)

#     def __str__(self):
#         return self.voyage_number

#     def __unicode__(self):
#         return self.voyage_number

#     class Meta:
#         ordering = ['-voyage_number']


# class Port(models.Model):

#     name = models.CharField(max_length=250)
#     price = models.CharField(max_length=10)
#     position = models.CharField(max_length=20)
#     country = models.CharField(max_length=20)
#     comment = models.TextField()
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)     
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     draft = models.BooleanField(default=False)
#     deleted = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

#     # def book_summarys(self):
#     #     story = self.story
#     #     return story[:180]

#     # def dice_result(self):
#     #     count = 0
#     #     sum = 0
#     #     try:
#     #         for comment in self.comment_set.all():
#     #             count += 1
#     #             sum += int(comment.dice)
#     #             result = sum/float(count)
#     #         return result
#     #     except:
#     #         return '--'

#     class Meta:
#         ordering = ['name']

class Charterer(models.Model):

    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    country = models.CharField(max_length=20)
    switch_board = models.CharField(max_length=30)
    contact_person = models.CharField(max_length=100)
    comment = models.TextField()
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