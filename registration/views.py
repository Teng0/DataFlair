from django.shortcuts import render
from . import forms

# Create your views here.

def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = "We Have recived this form again"
        if form.is_valid():
            html = html + 'The form is valid'
    else:
        html = "Welcome First Time"

    return  render(request,'registration\signUp.html',{'html':html,'form':form})



