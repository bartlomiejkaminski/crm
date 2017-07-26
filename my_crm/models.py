from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Company(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    name = models.CharField(max_length=200, blank=True, default='')
    email = models.EmailField(max_length=100, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    address = models.TextField()
    code = models.TextField()
    city = models.CharField(max_length=200, blank=True, default='')
    voivodeship = models.CharField(max_length=50, blank=True, default='')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='companies')

    class Meta:
        ordering = ('-created',)