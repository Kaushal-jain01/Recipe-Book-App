from django.db import models

# Create your models here.
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     email = models.EmailField(unique=True)
#     address = models.TextField(null=True, blank=True)
#     image = models.ImageField(upload_to='students/', blank=True, null=True)
#     file = models.FileField(null=True, blank=True, upload_to='student_files/')


class Car(models.Model):
    car_name = models.CharField(max_length=50)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.car_name} ({self.speed})"