from django.shortcuts import render
from .models import Blog
#get_object_or_404
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url="accounts:login")
def blog(request):
    blogs=Blog.objects.all()
    context={'blogs':blogs}
    return render(request, "blogs.html", context)


@login_required(login_url="accounts:login")
def blog_detail(request,id):
    blog=get_object_or_404(Blog, id=id)
    context={'blog':blog}
    return render(request, "blog_detail.html",context)



@login_required(login_url="accounts:login")
def search(request):
    quary=request.GET['search_value']
    blogs=Blog.objects.filter(Q(title__icontains=quary) | Q(topic__icontains=quary) | Q(short_description__icontains=quary))
    context={'blogs':blogs}
    return render(request, "blogs.html", context)
    
    
