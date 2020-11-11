from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
# from .forms import *


# Create your views here.

def home(request):
    return render(request, 'book/home.html')


def new(request):
    if request.method == "POST":
        output = request.POST
        firstName = output['firstName']
        middleName = output['middleName']
        lastName = output['lastName']
        contact1 = output['contact1']
        contact2 = output['contact2']
        email = output['email']
        address = output['address']
        group = output['group']

        if firstName == "" or contact1 == "":
            return HttpResponse("First Name & Contact Number 1 cannot be empty")
        else:
            contact = Contact.objects.create(
                firstName=firstName,
                middleName=middleName,
                lastName=lastName,
                contact1=contact1,
                contact2=contact2,
                email=email,
                address=address,
                group=group,
            )
            contact.save()
            return HttpResponse("Contact added successfully.")
    else:
        return render(request, 'book/new-contact.html')


def contactList(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, 'book/contact-list.html', context)
