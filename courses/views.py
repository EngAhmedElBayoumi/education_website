from django.shortcuts import render
from .models import courses as Courses , Lectures
#return json
from django.http import JsonResponse
#import json
import json
#login required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import profile as Profile
from django.db.models import Q
# Create your views here.


@login_required(login_url="accounts:login")
def courses(request):
    course=Courses.objects.all()
    context={'courses':course}

    return render(request, "courses.html", context)


@login_required(login_url="accounts:login")
def course_detail(request,id):
    course=Courses.objects.get(id=id)
    #get first lectures of this course
    lectures=Lectures.objects.filter(course=course)
    #get user that create this course
    instructor=User.objects.get(id=course.instructor.id)    
    #get instructor profile
    instructor_profile=Profile.objects.get(user=instructor)
    context={'course':course, 'lectures':lectures, 'instructor':instructor, 'instructor_profile':instructor_profile}
    return render(request, "course_detail.html", context)


def search(request):
    quary = request.GET['search_value']
    courses=Courses.objects.filter(Q(title__icontains=quary) | Q(description__icontains=quary) | Q(skill_level__icontains=quary) | Q(department__icontains=quary) | Q(grade__icontains=quary))
    context={'courses':courses}
    return render(request, "courses.html", context)
    



@login_required(login_url="accounts:login")
def get_lecture(request,id):
    lecture=Lectures.objects.get(id=id)
    context={'lecture':lecture}
    #return json response with lecture details
    return JsonResponse({'lecture':lecture.title, 'video':lecture.video.url})


