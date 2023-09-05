from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages


def index(request):
    messages.success(request, "Value for money Products")
    return render(request, "index.html")



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Form submitted, We will look after your problem ")
    return render(request, "contact.html")
