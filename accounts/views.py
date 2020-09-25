from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import  UserForm, User_Profile_Form
from django.forms import forms
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages


from . import views
import json
from .models import Registration,test
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from PayTm import Checksum

from .models import Registration,User_Profile
from .models import Tuition_Fee_Pay


MERCHANT_KEY ='iJXfRP%m4#c5rQE%';

# Create your views here.
@login_required()
def edit_profile(request):
   # context={}

    data1 = User_Profile.objects.get(user__id=request.user.id)
    #context1["data1"]=data1
    data=User.objects.get(username=request.user)
   # context["data"]=data
    return render(request, "edit_profile.html",{'data':data,'data1':data1})




@login_required()
def edit_profile_submit(request):
    data1 = User_Profile.objects.get(user__id=request.user.id)
    data = User.objects.get(username=request.user)

    if request.method=='POST':
       # first_name      = request.POST['first_name']
       # last_name       = request.POST['last_name']
        course_enrolled = request.POST['course_enrolled']
        gender          = request.POST['gender']
        blood_group     = request.POST['blood_group']
        about_yourself  =request.POST['about_yourself']
        date_of_birth   = request.POST['date_of_birth']
        date_of_joining = request.POST['date_of_joining']
        aadhar_number   = request.POST['aadhar_number']
        mobile_number   = request.POST['mobile_number']
        emergency_number= request.POST['emergency_number']
        profile_pic=request.FILES.get('profile_pic',None)

        #fs = FileSystemStorage()
        #filename = fs.save(profile_pic.name, profile_pic)

        #uploaded_file_url = fs.url(filename)
        father_name = request.POST['father_name']
        father_mobile_number = request.POST['father_mobile_number']
        mother_name = request.POST['mother_name']
        p_address = request.POST['p_address']
        p_city = request.POST['p_city']
        p_state = request.POST['p_state']
        p_pincode = request.POST['p_pincode']
        c_address = request.POST['c_address']
        c_city = request.POST['c_city']
        c_state = request.POST['c_state']
        c_pincode = request.POST['c_pincode']
        graduation_college = request.POST['graduation_college']
        graduation_course = request.POST['graduation_course']
        marks_graduation = request.POST['marks_graduation']
        graduation_marksheet = request.FILES.get('graduation_marksheet',None)


       # fs = FileSystemStorage()
        #filename = fs.save(graduation_marksheet.name, graduation_marksheet)
        #uploaded_file_url = fs.url(filename)
        senior_sec_name = request.POST['senior_sec_name']
        senior_sec_stream = request.POST['senior_sec_stream']
        marks_senior_sec = request.POST['marks_senior_sec']
        senior_sec_marksheet = request.FILES.get('senior_sec_marksheet')


        #fs = FileSystemStorage()
        #filename = fs.save(senior_sec_marksheet.name, senior_sec_marksheet)
        #uploaded_file_url = fs.url(filename)

        secondary_school_name = request.POST['secondary_school_name']

        marks_secondary = request.POST['marks_secondary']
        secondary_marksheet = request.FILES.get('secondary_marksheet',None)


        #fs = FileSystemStorage()
        #filename = fs.save(secondary_marksheet.name, secondary_marksheet)
        #uploaded_file_url = fs.url(filename)
        current_school_name = request.POST['current_school_name']
        current_school_marks = request.POST['current_school_marks']




        #saving data

    data1.course_enrolled =course_enrolled
    data1.gender = gender
    data1.blood_group =blood_group
    data1.about_yourself =about_yourself
    data1.date_of_birth =date_of_birth
    data1.date_of_joining =date_of_joining
    data1.aadhar_number =aadhar_number
    data1.mobile_number =mobile_number
    data1.emergency_number =emergency_number
    data1.profile_pic =profile_pic

    #fs = FileSystemStorage()
    #filename = fs.save(profile_pic.name, profile_pic)

   # data1.uploaded_file_url = fs.url(filename)
    data1.father_name = father_name
    data1.father_mobile_number = father_mobile_number
    data1.mother_name =mother_name
    data1.p_address =p_address
    data1.p_city = p_city
    data1.p_state =p_state
    data1.p_pincode =p_pincode
    data1.c_address =c_address
    data1.c_city = c_city
    data1.c_state =c_state
    data1.c_pincode =c_pincode
    data1.graduation_college =graduation_college
    data1.graduation_course =graduation_course
    data1.marks_graduation = marks_graduation
    data1.graduation_marksheet =graduation_marksheet

    #fs = FileSystemStorage()
    #filename = fs.save(graduation_marksheet.name, graduation_marksheet)
    #uploaded_file_url = fs.url(filename)
    data1.senior_sec_name = senior_sec_name
    data1.senior_sec_stream =senior_sec_stream
    data1.marks_senior_sec = marks_senior_sec
    data1.senior_sec_marksheet = senior_sec_marksheet

    #fs = FileSystemStorage()
    #filename = fs.save(senior_sec_marksheet.name, senior_sec_marksheet)
    #uploaded_file_url = fs.url(filename)

    data1.secondary_school_name =secondary_school_name

    data1.marks_secondary = marks_secondary
    data1.secondary_marksheet = secondary_marksheet

    #fs = FileSystemStorage()
    #filename = fs.save(secondary_marksheet.name, secondary_marksheet)
    #uploaded_file_url = fs.url(filename)
    data1.current_school_name = current_school_name
    data1.current_school_marks =current_school_marks

    data1.save();
    print("updated")
    #context["status"]="changes saved successfully"
    return redirect('profile')





def account_login(request):
     if request.method=='POST':
         # rechaptcha stuff
        # clientKey = request.POST['g-recaptcha-response']
         #secretKey = '6LeRCPgUAAAAAEOeZRzaVU0SDT4LhlMlepqbaoUu'
         #capchadata = {
          #   'secret': secretKey,
           #  'response': clientKey,
         #}

         #r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=capchadata)
         #response = json.loads(r.text)
         #verify = response['success']
         #print('your success is ', verify)
         user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
         if user is not None:
             auth.login(request,user)
             return redirect('/')
         else:

             messages.info(request,' oops!! invalid Username/Password Please try again.')
             return redirect('account_login')

     else:
         return render(request,'login.html')

def logout(request):
     auth.logout(request)
     return redirect('/')
@login_required(login_url='login')
def profile(request):
    return render(request,"profile.html")


def signup(request):
    if request.method=='POST':
        # rechaptcha stuff
       # clientKey = request.POST['g-recaptcha-response']
        #secretKey = '6LeRCPgUAAAAAEOeZRzaVU0SDT4LhlMlepqbaoUu'
        #capchadata = {
         #  'secret': secretKey,
          #  'response': clientKey,
        #}

        #r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=capchadata)
        #response = json.loads(r.text)
        #verify = response['success']
        #print('your success is ', verify)
        if request.POST['password']==request.POST['confirm_password']:
            try:
                user=User.objects.get(username=request.POST['username'])
                messages.info(request,'username already exist!! please choose another one')
                return render(request,'register.html')
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'],first_name=request.POST['first_name'],last_name=request.POST['last_name'])


                auth.login(request,user)
                return render(request,'login.html')





        else:

            return render(request,'register.html')
    else:
        return render(request,'register.html')










@login_required(login_url='accounts/login')
def showuserdata(request):
    datas=User_Profile.objects.filter(user=request.user)
    data1 = User.objects.filter(username=request.user)
    return render(request,"profile.html",{'data':datas,'datauser':data1})






#paytm integration module
def Checkout(request):

    if request.method=="POST":


        payment_month =request.POST['payment_month']


        email =request.POST['email']
        full_name=request.POST['full_name']
        mobile_number =request.POST['mobile_number']
        amount =request.POST['amount']
        course_enrolled=request.POST['course_enrolled']
        order=Tuition_Fee_Pay(payment_month=payment_month,course_enrolled=course_enrolled,full_name=full_name,email=email,mobile_number=mobile_number,amount=amount)
        order.save()
        id=order.feepayment_id
        thank=True


        #return render(request,'profile.html',{'thank':thank,'id':id})

        param_dict={
            'MID':'cnBRAh22465235871830',
            'ORDER_ID':str(order.feepayment_id),
            'TXN_AMOUNT':str(amount),
            'CUST_ID':email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'DEFAULT',
            'CHANNEL_ID':'WEB',
            'MOBILE_NO':str(order.mobile_number),

	        'CALLBACK_URL':'https://studypointgaya.herokuapp.com/accounts/handlerequest/',

        }


        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict,MERCHANT_KEY)
        return render(request, 'paytm.html',{'param_dict': param_dict})

    return render(request,'profile.html')

    return render(request,'profile.html')




@csrf_exempt
def handlerequest(request):


    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':

            checksum = form[i]



    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY,checksum)
    if verify:

        if response_dict['RESPCODE'] == '01':

            print('order successful')

        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html',{'response': response_dict})


#password  reset authentication

