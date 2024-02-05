from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class EmployeeProfile(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null = True , blank=True)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employee_images/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
