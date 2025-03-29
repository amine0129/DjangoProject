from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import get_subscribers,delete_subscriber
from .mongodb import subscribers
def login(response):
 return render(response,'App/login.html')
def listsub(response):
    return render(response,"App/listsubscribers.html",{'subscribers':list(subscribers.find())})
def supprimer(response,name):
   delete_subscriber(name)
   return redirect('listsub')
# Create your views here.
