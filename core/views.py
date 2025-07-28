from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from .forms import AppointmentForm

def home(request):
    services = [
        {'icon': '🪥', 'name': 'Teeth Cleaning', 'description': 'Professional cleaning for a healthy, bright smile.'},
        {'icon': '🛠️', 'name': 'Root Canal', 'description': 'Pain-free RCT procedures with modern equipment.'},
        {'icon': '✨', 'name': 'Cosmetic Dentistry', 'description': 'Whitening, reshaping, and restoring your smile.'},
    ]
    return render(request, 'core/home.html', {'services': services})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            form = ContactForm()  # Clear the form after submit
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment has been booked!')
            form = AppointmentForm()
    else:
        form = AppointmentForm()
    return render(request, 'core/appointment.html', {'form': form})


from .models import GalleryImage

def services(request):
    gallery_images = GalleryImage.objects.order_by('-uploaded_at')
    return render(request, 'core/services.html', {'gallery_images': gallery_images})
