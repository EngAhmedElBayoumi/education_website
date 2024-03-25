from django.shortcuts import render
#login required
from django.contrib.auth.decorators import login_required
from .models import Contact
#import message
from django.contrib import messages
# Create your views here.



@login_required(login_url="accounts:login")
def home(request):
    return render(request,'index.html')





@login_required(login_url="accounts:login")
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        messages.success(request,"Your message has been sent successfully")
        return render(request,'contact.html')
    
    return render(request,'contact.html')




@login_required(login_url="accounts:login")
def error_404(request,exception):
    return render(request,'error_404.html')

@login_required(login_url="accounts:login")
def error_500(request):
    return render(request,'error_500.html')