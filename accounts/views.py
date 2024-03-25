from django.shortcuts import render
from .models import profile as Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.error(request, "Username or password is incorrect")
    return render(request, "login.html")

@login_required(login_url="accounts:login")
def log_out(request):
    logout(request)
    return render(request, "login.html")


def sign_up(request):
    #get fname , last name, username, email, password, confirm password 
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        #check if there any value is empty
        if username == "" or email == "" or password == "" or confirm_password == "" or fname == "" or lname == "":
            messages.error(request, "Please fill all the fields")
            return render(request, "signup.html")
        
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.error(request, "Username already exists")
            elif User.objects.filter(email = email).exists():
                messages.error(request, "Email already exists")
            else:
                user = User.objects.create_user(username = username, email = email, password = password, first_name = fname, last_name = lname)
                user.save()
                #create profile
                Profile.objects.create(user = user)
                messages.success(request, "User created successfully")
                return redirect('accounts:login')
        else:
            messages.error(request, "Password and Confirm Password do not match")
    
    return render(request, "signup.html")

@login_required(login_url="accounts:login")
def profile(request):
    user = request.user
    profile = Profile.objects.get(user = user)
    
    #upade profile if form is submitted
    if request.method == "POST":
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        user.save()
        
        profile.bio = request.POST['bio']
        profile.save()
        
        if 'image' in request.FILES:
            profile.image = request.FILES['image']
            profile.save()
        
        messages.success(request, "Profile updated successfully")
        return redirect('accounts:profile')
    
    
    context = {'profile':profile}
    return render(request, "profile.html", context)