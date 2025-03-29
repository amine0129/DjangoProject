from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import get_subscribers,delete_subscriber
from .mongodb import subscribers,admins
def login(response):
 return render(response,'App/login.html')

def listsub(response):
    subscriber=list(subscribers.find({}))
    for sub in subscriber :
            sub['id']=str(sub.pop("_id"))
    if response.method=='POST':
        user=response.POST.get('username')
        password=response.POST.get('password')
        print(f"Username: {response.POST.get('username')}, Password: {response.POST.get('password')}") 
        if admins.find_one({'UserName':user,'password':password}):
          return render(response,"App/listsubscribers.html",{'subscribers':subscriber})
        else:
            return render(response,'App/login.html',{'msg':'password or username undifiend'})
    
def supprimer(response,sub_id):
   delete_subscriber(sub_id)
   return redirect('listsub')

def createsub(response):
    return render(response,'App/createsub.html')
# Create your views here.
