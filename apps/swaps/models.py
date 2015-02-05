from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='photos', blank=True, null=True)
    user = models.ForeignKey(User)
    description = models.TextField(max_length=250)
    condition = models.CharField(max_length=50)  # change to multi choice.
    status = models.CharField(max_length=50) # change to multi choice.

# class ItemGroup(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(max_length=250)
#     items = models.ManyToManyField('Item')


class Swap(models.Model):
    name = models.CharField(max_length=50)
    STATUS_CHOICES = (
        ('AVAILABLE', 'Available'),
        ('CLOSED', 'Closed'),
        ('PENDING', 'Pending'),
    )
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='AVAILABLE')
    initiator = models.ForeignKey(User, related_name="initiator_swap")
    initiator_items = models.ManyToManyField(Item, related_name="initiator_items_swap")
    other_party_items = models.ManyToManyField(Item, related_name="other_party_items_swap")
    other_party = models.ForeignKey(User, related_name="other_party_swap")

