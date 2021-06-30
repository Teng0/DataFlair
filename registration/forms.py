from django import forms
from django.core import validators




class SignUp(forms.Form):

    def check_size(value):
        if len(value) < 6:
            raise forms.ValidationError("the Password is too short")

    first_name =  forms.CharField(initial = 'First Name', )
    last_name = forms.CharField()
    email = forms.EmailField(help_text='write your email', )
    address = forms.CharField(required=False)
    Technology = forms.CharField(initial='Django')
    age = forms.IntegerField()
   # password = forms.CharField(widget=forms.PasswordInput, validators = [validators.MinLengthValidator(6)])
    password = forms.CharField(widget=forms.PasswordInput, validators = [check_size])
    re_password = forms.CharField(help_text='renter your password ', widget= forms.PasswordInput)



    def clean_password(self):
        password =  self.cleaned_data['password']

        if len(password) < 4:
            raise  forms.ValidationError('password is to Short')

        return password
