from django.contrib.auth.models import User
from .models import User_Profile
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',

            'email',
        ]


class User_Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = [
            'course_enrolled',
            'gender',
            'blood_group',
            'about_yourself',
            'date_of_birth',
            'date_of_joining',
            'aadhar_number',
            'mobile_number',
            'emergency_number',
            'profile_pic',
            'father_name',
            'father_mobile_number',
            'mother_name',
            'p_address',
            'p_state',
            'p_city',
            'p_pincode',
            'c_address',
            'c_state',
            'c_city',
            'c_pincode',
            'graduation_college',
            'graduation_course',
            'graduation_marksheet',
            'marks_graduation',
            'senior_sec_name',
            'marks_senior_sec',
            'senior_sec_marksheet',
            'senior_sec_stream',
            'marks_secondary',
            'secondary_school_name',
            'secondary_marksheet',
            'current_school_name',
            'current_school_marks',
        ]
