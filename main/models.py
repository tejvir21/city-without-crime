from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Police Station Model
class PoliceStation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    head_officer = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Complaint Model
class Complaint(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    police_station = models.ForeignKey(PoliceStation, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('In Progress', 'In Progress'),
            ('Resolved', 'Resolved')
        ],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Complaint {self.id} - {self.status}"


# Criminal Model
class Criminal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    crime_level = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='criminals/')

    def __str__(self):
        return self.name


# Emergency News Model
class Emergency(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Emergency {self.id}"


# Login Master Model (Optional for additional admin management)
class LoginMaster(models.Model):
    username = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.username
