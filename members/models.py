from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Address(models.Model):
    street = models.CharField(max_length=500,blank=True)
    city = models.CharField(max_length=50,blank=True)
    state = models.CharField(max_length=2,blank=True)
    zip = models.CharField(max_length=5,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="address_for_user", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street},{self.city},{self.state}"


class Membership(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    is_donor = models.BooleanField(default=False)
    is_volunteer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)


# class Member(models.Model):
#     first_name = models.CharField(max_length=250)
#     last_name = models.CharField(max_length=250)
#     date_of_birth = models.CharField(max_length=10)
#     phone_number = models.CharField(max_length=250, blank=True)
#     email_address = models.CharField(max_length=30)
#     date_created = models.DateField(auto_now_add=True)
#     is_admin = models.BooleanField(default=False)
#     # membership = models.OneToOneField(Membership, on_delete=models.CASCADE)
#     address = models.ManyToManyField(Address)
#
#     def __str__(self):
#         return self.first_name
#
#     def get_absolute_url(self):
#         return reverse('members:members_detail', args=[str(self.id)])
class User(AbstractUser):
    address = models.ForeignKey(Address,related_name='address_for_user',on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    date_created = models.DateField(auto_now_add=True,null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


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
