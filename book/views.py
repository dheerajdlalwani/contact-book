from django.shortcuts import render, redirect, HttpResponse
from .models import *
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
        print(output)
        return HttpResponse("Contact added successfully.")
    else:
        return render(request, 'book/new-contact.html')