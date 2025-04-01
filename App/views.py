from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import get_subscribers,delete_subscriber
from .mongodb import subscribers,admins,Categories
from datetime import datetime
from bson import ObjectId
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
    else:
        return render(response,"App/listsubscribers.html",{'subscribers':subscriber})
def supprimer(response,sub_id):
   delete_subscriber(sub_id)
   return redirect('listsub')

def createsub(response):
    categories=list(Categories.find({}))
    return render(response,'App/createsub.html',{'categories':categories})

def addsub(response):
    if response.method=='POST':
        fullname=response.POST.get('fullname')
        phone=response.POST.get('phone')
        category=response.POST.get('category')
        subscribers.insert_one({
            'fullname':fullname,
            'phone':phone,
            'category':category,
            'inscriptionDate': datetime.now()
        })
        return redirect('listsub')
def editsub(response,sub_id):
    categories=list(Categories.find({}))
    sub=subscribers.find({"_id":ObjectId(sub_id)})
    return render(response,'App/editsub.html',{'categories':categories,'sub':sub[0],'sub_id':sub_id})
def updatesub(response,sub_id):
    if response.method == 'POST':
        fullname=response.POST.get('fullname')
        phone=response.POST.get('phone')
        category=response.POST.get('category')
        subscribers.update_one({'_id':ObjectId(sub_id)},{"$set":{ 
            'fullname':fullname,
            'phone':phone,
            'category':category,}})
        return redirect('listsub')
# Create your views here.
