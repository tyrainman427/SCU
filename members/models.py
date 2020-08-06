from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Address(models.Model):
    street = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.street},{self.city},{self.state}"


class Membership(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    is_donor = models.BooleanField(default=False)
    is_volunteer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)


class Member(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=250, blank=True)
    email_address = models.CharField(max_length=30)
    date_created = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    # membership = models.OneToOneField(Membership, on_delete=models.CASCADE)
    address = models.ManyToManyField(Address)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('members:members_detail', args=[str(self.id)])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

class Contact(models.Model):
    subject = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=15)
    message = models.CharField(max_length=500)
    from_email = models.EmailField(max_length=15)

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
