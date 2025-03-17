from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'roll_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Roll'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your phone number'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select a date'}),
        }