from django import forms

from .models import SignUp
class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()



class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']

    def clean_email(self):
#add functions and constrains on the emails added
        email= self.cleaned_data.get('email')
        email_base,provider = email.split('@')
        domain , extention = provider.split('.')
        if  extention != "com" or domain != "gmail":
            raise forms.ValidationError("Please enter a gmail account")
        return email
#you can make clean for any time
#    def clean_full_name(self):
#        return self.clean_data.get('full_name')
