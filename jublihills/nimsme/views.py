from django.http import HttpResponse
from django.shortcuts import render
from .models import Uploadimage, User
from django.http import HttpResponse

# Create your views here.
from django.template import loader

def first(request):
    return render(request, 'jsd.html')
def second(request):
    return render(request, 'program.html')
#def upload_image(request):


def userreg(request):
    return render(request, "reg.html", {})


def insertuser(request):
    vuid = request.POST['tuid'];
    vuname = request.POST['tuname'];
    vuemail=request.POST['tuemail'];
    vucontact = request.POST['tucontact'];
    us = User(uid=vuid, uname=vuname, uemail=vuemail, ucontact=vucontact);
    us.save();
    return render(request, 'reg.html', {})
