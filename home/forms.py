from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    username=forms.EmailField(max_length=30)
    dob=forms.DateField(required=False,widget=forms.D(attrs={
        'class':'datepicker', 'data-min': '1960-01-01',
        'data-max': '2000-12-12'}))
    profpic=forms.ImageField(required=False)


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email', 'password1', 'password2', 'dob','profpic' )



