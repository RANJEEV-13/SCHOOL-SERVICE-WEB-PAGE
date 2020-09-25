from django.urls import path
from . import views

urlpatterns=[path("",views.index,name="index"),
             path('index.html',views.index,name="index"),

             path('about.html',views.about,name="about"),
             path('courses.html',views.courses,name="courses"),
             path('teacher.html',views.teacher,name="teacher"),
             path('blog.html',views.blog,name="blog"),
             path('contact.html',views.contact,name="contact"),
             path('blog_single.html',views.blog_single,name="blog_single"),
             path('careers.html',views.careers,name="careers"),
             path('enquiry_submit',views.enquiry_submit,name='enquiry_submit'),
             path('register.html',views.register,name='register'),
             path('career_submit',views.career_submit,name='career_submit'),
             path('callback_request_submit',views.callback_request_submit,name='callback_request_submit'),
             path('downloads.html',views.downloads,name="downloads"),
             path('home.html',views.home,name="home"),
             path('index.html',views.notice,name="notice"),
             path('course-single.html',views.course_single,name="course_single"),


             ]

