from django.shortcuts import render
#user
from django.contrib.auth.models import User
#profile
from accounts.models import profile as Profile
from django.db.models import Q
# Create your views here.

def instructor(request):
    #get all users that create courses
    instructors=User.objects.filter(is_staff=True)
    instructors_profile=[]
    for instructor in instructors:
        #check if this user is has profile
        if Profile.objects.filter(user=instructor).exists():
            instructors_profile.append(Profile.objects.get(user=instructor))
        
    
    context={'instructors':instructors, 'instructors_profile':instructors_profile}
    return render(request, "instructors.html", context)



def search(request):
    qeary=request.GET['search_value']
    #get all users that create courses
    instructors=User.objects.filter(is_staff=True)
    instructors_profile=[]
    for instructor in instructors:
        #check if this user is has profile
        if Profile.objects.filter(user=instructor).exists():
            instructors_profile.append(Profile.objects.get(user=instructor))
        
    
    context={'instructors':instructors, 'instructors_profile':instructors_profile}
    return render(request, "instructors.html", context)


def instructor_detail(request,id):
    instructor=User.objects.get(id=id)
    #check if this user is has profile
    if Profile.objects.filter(user=instructor).exists():
        instructor_profile=Profile.objects.get(user=instructor)
    else:
        instructor_profile=None
    context={'instructor':instructor, 'instructor_profile':instructor_profile}
    return render(request, "instructor_detail.html", context)

