from django import forms
from .models import ContactMessage
from .models import Appointment

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'phone', 'service', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
