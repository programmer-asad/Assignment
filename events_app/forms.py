from django import forms
from django.contrib.auth.models import User
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'description', 'category', 'capacity']    
         
    date = forms.DateField(widget=forms.DateInput(
                            attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD' }, format='%Y-%m-%d'))
    description = forms.CharField(widget=forms.TextInput) 
    


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
