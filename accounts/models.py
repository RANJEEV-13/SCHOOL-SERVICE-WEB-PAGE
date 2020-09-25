from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class test(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)


class User_Profile(models.Model):
    #first_name=models.CharField(max_length=100)
    #last_name=models.CharField(max_length=100)
    course_enrolled=models.CharField(max_length=100,blank=True,null=True)
    gender=models.CharField(max_length=20,blank=True,null=True)
    blood_group=models.CharField(max_length=10,blank=True,null=True)
    about_yourself=models.CharField(max_length=200,blank=True,null=True)
    date_of_birth=models.DateField(blank=True,null=True,auto_now_add=False)
    date_of_joining=models.DateField(blank=True,null=True,auto_now_add=False)
    aadhar_number=models.CharField(max_length=12,blank=True,null=True)
    mobile_number=models.CharField(max_length=10,blank=True,null=True)
    emergency_number = models.CharField(max_length=10,blank=True,null=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True,null=True,default='profile_pic/default_profile_pic.png')
    father_name = models.CharField(max_length=100,blank=True,null=True)
    father_mobile_number = models.CharField(max_length=10,blank=True,null=True)
    mother_name = models.CharField(max_length=100,blank=True,null=True)
    p_address = models.CharField(max_length=200,blank=True,null=True)
    p_city = models.CharField(max_length=100,blank=True,null=True)
    p_state = models.CharField(max_length=100,blank=True,null=True)
    p_pincode = models.CharField(max_length=6,blank=True,null=True)
    c_address = models.CharField(max_length=200,blank=True,null=True)
    c_city = models.CharField(max_length=100,blank=True,null=True)
    c_state = models.CharField(max_length=100,blank=True,null=True)
    c_pincode = models.CharField(max_length=6,blank=True,null=True)
    graduation_college = models.CharField(max_length=100,blank=True,null=True)
    graduation_course = models.CharField(max_length=100,blank=True,null=True)
    marks_graduation = models.CharField(max_length=10,blank=True,null=True)
    graduation_marksheet = models.FileField(upload_to='graduation_marksheet',blank=True,null=True)
    senior_sec_name = models.CharField(max_length=100,blank=True,null=True)
    senior_sec_stream = models.CharField(max_length=100,blank=True,null=True)
    marks_senior_sec = models.CharField(max_length=10,blank=True,null=True)
    senior_sec_marksheet = models.FileField(upload_to='senior_sec_marksheet',blank=True,null=True)

    secondary_school_name = models.CharField(max_length=100,blank=True,null=True)

    marks_secondary = models.CharField(max_length=10,blank=True,null=True)
    secondary_marksheet = models.FileField(upload_to='secondary_marksheet',blank=True,null=True)
    current_school_name = models.CharField(max_length=100,blank=True,null=True)
    current_school_marks = models.CharField(max_length=10,blank=True,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

class Tuition_Fee_Pay(models.Model):
    feepayment_id=models.AutoField(primary_key=True)
    payment_month=models.CharField(max_length=50)

    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile_number=models.CharField(max_length=10)
    amount = models.IntegerField()
    course_enrolled=models.CharField(max_length=50)





class Registration(models.Model):



    name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    address=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField()
    birth_date=models.DateField()
    contactno=models.CharField(max_length=10)
    course=models.CharField(max_length=100)
    #email=models.EmailField()
    candidate_pic = models.ImageField(upload_to='candidate_pic')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            User_Profile.objects.create(user=instance)

   # @receiver(post_save, sender=User)
    #def save_user_profile(sender, instance, **kwargs):
     #   instance.User_Profile.save()







