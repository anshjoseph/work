from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    #dict
    """
    context = {
        'var':"32"
    }
    cdn: content delivery network
    """
    messages.success(request,"hello error")
    return render(request,'index.html')
def about(request):
   return render(request,'about.html')
def services(request):
    return render(request,'service.html')
def contact(request):
    if request.method == 'POST':
        ques = request.POST.get('ques')
        contact = Contact(ques=ques,data=datetime.today())
        contact.save()
        messages.success(request,'sent')
    return render(request,'contact.html')
