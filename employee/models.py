from django.db import models
from django.urls import reverse


class Employee(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    birth_date = models.DateTimeField()
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    title = models.CharField(max_length=30, blank=True)
    employee_id = models.CharField(max_length=10)
    start_date = models.DateTimeField()
    department = models.CharField(max_length=50)
    work_location = models.CharField(max_length=50)
    supervisor = models.CharField(max_length=50)
    emergency_contact_name = models.CharField(max_length=50)
    emergency_contact_number = models.CharField(max_length=50)
    salary = models.FloatField(default="$0.00", blank=True)
    phone_number = models.CharField(max_length=250, blank=True)
    email_address = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('employee:employee_detail', args=[str(self.id)])
