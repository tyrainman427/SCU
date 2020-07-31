from django.contrib import admin
from .models import Member, Address, Membership
# Register your models here.
admin.site.register(Member)
admin.site.register(Membership)
admin.site.register(Address)
