from django.contrib import admin
from .models import Member, Address, Profile
# Register your models here.
admin.site.register(Member)
admin.site.register(Address)
admin.site.register(Profile)
