from django.db import models
from django.utils import timezone
# Create your models here.
class Notice(models.Model):
    description=models.CharField(max_length=200)
class Course(models.Model):
    Course_Name=models.CharField(max_length=100)
    Course_Teacher_Name=models.CharField(max_length=100)
    Seat=models.IntegerField()
    Course_Duration=models.IntegerField()
    Course_Description=models.TextField()
    Course_Image=models.ImageField(upload_to='pics')
    Course_fee=models.IntegerField()

class Teacher(models.Model):
    Teacher_Name=models.CharField(max_length=100)
    Teacher_Designation=models.CharField(max_length=50)
    Teacher_Description=models.CharField(max_length=100)
    Teacher_Image=models.ImageField(upload_to='pics')



class enquiry(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    contactno=models.CharField(max_length=10)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)


class Career(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    contactno=models.CharField(max_length=10)
    address=models.TextField()
    resume=models.FileField(upload_to='resume')


class Callback_Request(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    message=models.TextField()


class Downloads(models.Model):
    file_link_name=models.CharField(max_length=100)
    upload_file = models.FileField(upload_to='downloads')
    file_download_name=models.CharField(max_length=500)


