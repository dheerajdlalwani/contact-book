from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
from .forms import *


# Create your views here.

def home(request):
    return render(request, 'book/home.html')


def new(request):
    form = NewContactForm()
    if request.method == "POST":
        form = NewContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(contactList)
        else: 
            return HttpResponse("The form is not valid!")
    context = {"form": form}
    return render(request, 'book/new-contact.html', context)

def contactList(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, 'book/contact-list.html', context)
