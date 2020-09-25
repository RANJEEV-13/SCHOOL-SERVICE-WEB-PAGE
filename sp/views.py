from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage


# Create your views here.
from sp.models import Course,Teacher,Career,Callback_Request
from .models import enquiry,Downloads,Notice


def index(request):
    teachers = Teacher.objects.all()
    coursess = Course.objects.all()
    notices = Notice.objects.all()
    return render(request, "index.html", {'coursess': coursess,'teachers':teachers,'notices':notices})

    return render(request,"index.html")


def about(request):
    return render(request,"about.html")

def course_single(request):
    coursess = Course.objects.all()
    return render(request,"course-single.html",{'coursess':coursess})

def courses(request):

    coursess=Course.objects.all()
    return render(request,"courses.html",{'coursess':coursess})

def teacher(request):
    teachers=Teacher.objects.all()
    return render(request,"teacher.html",{'teachers':teachers})
def notice(request):
    notices=notice.objects.all()
    return render(request,"index.html",{'notices':notices})



def blog(request):
    return render(request,"blog.html")

def blog_single(request):
    return render(request,"blog_single.html")

def contact(request):
    return render(request,"contact.html")

def careers(request):
    return render(request,"careers.html")

def downloads(request):




        files = Downloads.objects.all()

        return render(request, "downloads.html", {'files': files})


def home(request):
    return render(request,"home.html")



def account_login(request):
    return render(request,"login.html")



def register(request):
    return render(request,'register.html')


def enquiry_submit(request):

    if request.method=='POST':

        name=request.POST['name']
        email=request.POST['email']
        contactno=request.POST['contactno']
        subject=request.POST['subject']
        message=request.POST['message']


        enquiry1=enquiry(name=name,email=email,contactno=contactno,subject=subject,message=message)
        print("query submitted!!!!!!!!!!!")
        enquiry1.save();
    return render(request,'contact.html')



def career_submit(request):
    if request.method=='POST' and request.FILES['resume']:

        first_name =request.POST['first_name']
        last_name = request.POST['last_name']
        email =request.POST['email']
        contactno =request.POST['contactno']
        address = request.POST['address']
        resume =request.FILES['resume']
        fs=FileSystemStorage()
        filename=fs.save(resume.name,resume)


        uploaded_file_url = fs.url(filename)

        career_submit1=Career(first_name=first_name,last_name=last_name,email=email,contactno=contactno,address=address,resume=resume)
        print("resume submitted")

        career_submit1.save();
    return  render(request,'index.html')

def callback_request_submit(request):
    if request.method=='POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        course=request.POST['course']
        phone=request.POST['phone']
        message=request.POST['message']
        callback_request_submit1=Callback_Request(first_name=first_name,last_name=last_name,course=course,phone=phone,message=message)
        print("request submitted")
        callback_request_submit1.save();
    return render(request,'index.html')

