from django.shortcuts import render
from .forms import SignUpForm , ContactForm
from .models import SignUp

def home (request):

    title = "Sign Up"
    form = SignUpForm(request.POST or None)
    #if request.user.is_authenticated():
    #    title = "hello there %s" %(request.user)
    context = {
        "title": title,
        "form" :form,
    }
    if form.is_valid(): #u can add form.cleaned_data.get() to make the Validation
        instance=form.save(commit = True)
        context ={
            "title":"Thank You"
        }

    if request.user.is_authenticated():
        print "helllo"
        queryset= SignUp.objects.all()
        context={
            "queryset":queryset,
        }
    return render(request,"home.html",context)



def contact (request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key in form.cleaned_data:
            print key,form.cleaned_data.get(key)
    context = {
        "form":form,
        "title":title,
    }
    return render(request,"forms.html",context)
