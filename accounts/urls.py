

from django.urls import  path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("account_login",views.account_login,name='account_login'),
    path("logout",views.logout,name='logout'),
    path("profile", views.showuserdata, name='profile'),
    path("signup",views.signup,name='signup'),
    path("edit_profile",views.edit_profile,name='edit_profile'),
    path("edit_profile_submit",views.edit_profile_submit,name='edit_profile_submit'),
#password reset  module


    path('reset_password',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html") ,name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),

#paytm module

path("Checkout",views.Checkout,name='Checkout'),
path('handlerequest/',views.handlerequest,name='handlerequest')


]