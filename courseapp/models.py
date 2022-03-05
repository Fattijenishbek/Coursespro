from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    imagepath=models.ImageField(null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    logo=models.ImageField(null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Branch(models.Model):
    latitude=models.CharField(max_length=250)
    longitude=models.CharField(max_length=250)
    address=models.CharField(max_length=200)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.address

class Contact(models.Model):
    contact_types=[
        (1, 'Phone'),
        (2, 'Facebook'),
        (3, 'Email')
    ]

    type=models.IntegerField(choices=contact_types)
    value=models.CharField(max_length=50)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE )

    def __str__(self):
        return self.value



