from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp


#this customise the admin stuff
class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","timestamp","full_name" ]
    form = SignUpForm
#    class Meta:
#        model=SignUp

admin.site.register(SignUp,SignUpAdmin)
