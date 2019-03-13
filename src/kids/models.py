from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super(AvailableManager,
                     self).get_queryset() \
            .filter(sponsor = None)

# Create your models here.

GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

class Kid(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='kids_kid',
                               blank=True, null = True)

    sponsor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='kid',
                               blank=True, null = True)
    name = models.CharField(max_length=150)
    date_of_birth = models.DateField(blank=True, null=True)
    gender=models.CharField(max_length=10,
                            choices=GENDER_CHOICES, blank=True, null=True)
    city=models.CharField(max_length=250,blank=True, null=True)
    photo = models.ImageField(
        "Kid picture", upload_to="kid_pics/%Y-%m-%d/", null=True, blank=True
    )
    description = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    objects = models.Manager() # The default manager.
    available = AvailableManager() # Our custom manager.

    def __str__(self):
        return self.name + ', ' + self.gender + ', ' + str(self.age)


    class Meta:
        ordering = ('-created',)

    @property
    def age(self):
        if(self.date_of_birth is None) : return 0
        return int((datetime.now().date() - self.date_of_birth).days / 365.25)




class Sponsorship(models.Model):

    SP_CHOICES = (
        ('s', 'Sponsored'),
        ('c', 'Cancelled'),
    )

    sponsor = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='sponsorship',
                               )
    kid = models.ForeignKey(Kid,
                               on_delete=models.CASCADE,
                               related_name='sponsorship',)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    ended = models.DateTimeField(auto_now=True, blank=True, null=True)

    action=models.CharField(max_length=10,
                            choices=SP_CHOICES, default='s')

class Payment(models.Model):

    sponsorship = models.ForeignKey(Sponsorship,
                               on_delete=models.CASCADE,
                               related_name='payments',
                               )    
    braintree_id = models.CharField(max_length=150, blank=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)    