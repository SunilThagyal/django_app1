from django.db import models
# Create your models here.
class Student(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone_number = models.IntegerField()

class StudentDetail(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="details")
    Email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=20)
    birth_date = models.DateField(null=True)
    division = models.CharField(max_length=20)
    semester = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50)

