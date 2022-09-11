from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import random
import string
import uuid


def generate_token():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))


class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    contact = PhoneNumberField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Exchange(models.Model):
    id = models.AutoField(primary_key=True)
    toy_to_change = models.CharField(max_length=255)
    desired_toy = models.CharField(max_length=255)
    owner = models.ForeignKey(Owner, related_name="toys",on_delete=models.CASCADE)
    token = models.CharField(max_length=255, default=generate_token, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    image_url = models.ImageField(upload_to='uploads')
    exchange = models.ForeignKey(Exchange, related_name="pictures",on_delete=models.CASCADE)
