from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password, is_password_usable





@receiver(post_save, sender=User)
def hash_password(sender, instance=None, created=False, **kwargs):
   ''' Hashes the password given when a User is created or updated '''
   if not is_password_usable(instance.password):
       instance.password = make_password(instance.password)
       instance.save()

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    ''' Creates a token whenever a User is created '''
    if created:
        Token.objects.create(user=instance)



@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """Creates a token whenever a User is created"""
    if created:
        Token.objects.create(user=instance)


class Item(models.Model):

    CONDITION_CHOICES = (
        ('Poor', 'Poor'),
        ('Fair', 'Fair'),
        ('Good', 'Good'),
        ('Excellent', 'Excellent'),
        ('Like New', 'Like New'),
        ('New', 'New')
    )



    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='photos', blank=True, null=True)
    user = models.ForeignKey(User)
    description = models.TextField(max_length=250)
    condition = models.CharField(max_length=15, choices=CONDITION_CHOICES)
    status = models.CharField(max_length=50) # change to multi choice.

    def __str__(self):
        return self.name

class Swap(models.Model):

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

    def __str__(self):
        return self.status

