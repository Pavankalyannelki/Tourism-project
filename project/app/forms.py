from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import HotelBooking


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='',required=True)
    username=forms.CharField(help_text='',required=True)
    password1=forms.CharField(help_text='',widget=forms.PasswordInput,required=True,label='Password')
    password2=forms.CharField(help_text='',widget=forms.PasswordInput,required=True,label='Confirm Password')
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class HotelBookingForm(forms.ModelForm):
    class Meta:
        model = HotelBooking
        fields = '__all__'  # Corrected typo here
        widgets = {
            'checkin_date': forms.DateInput(attrs={'type': 'date'}),
            'checkout_date': forms.DateInput(attrs={'type': 'date'}),
           
        }
