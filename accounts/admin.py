from django.contrib import admin


from .models import Registration,Tuition_Fee_Pay,User_Profile,test
# Register your models here.


admin.site.register(Registration)
admin.site.register(Tuition_Fee_Pay)
admin.site.register(User_Profile)
admin.site.register(test)
