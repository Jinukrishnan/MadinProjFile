from django.db import models
from django.urls import reverse


# Create your models here.

class Department(models.Model):
    D_name = models.CharField(max_length=250, unique=True)
    D_slug = models.SlugField(max_length=250, unique=True)
    D_image = models.ImageField(upload_to='department')
    Vacancy = models.IntegerField()
    Description = models.TextField()
    Vision = models.TextField()
    Mission = models.TextField()

    def __str__(self):
        return self.D_name

    def get_url(self):
        # return reverse('Department', args=[self.D_slug])
        return reverse('Department', args=[self.id])


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    C_slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    genter = models.CharField(max_length=100)
    phone = models.DecimalField(max_digits=20, decimal_places=10)
    email = models.CharField(max_length=250)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Purpose = models.CharField(max_length=250)
    Material = models.CharField(max_length=250)

    def __str__(self):
        return self.name
