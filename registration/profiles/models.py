from django.db import models

# Create your models here.

class Users(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    qualification=models.CharField(max_length=200)
    job=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    options=(
        ("male","male"),
        ("female","female"),
        ("other","other")
       )

    gender=models.CharField(max_length=200,choices=options,default="male")

    def __str__(self):
        return self.name



