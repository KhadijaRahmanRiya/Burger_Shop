from django.shortcuts import render, redirect 
from datetime import datetime
from .models import Contact  
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        if name and email and phone and desc:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, 'contact.html')

