from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="accounts:login")
def book(request):
    books = Book.objects.all()
    context={'books':books}
    
    return render(request, "books.html", context)

@login_required(login_url="accounts:login")
def search(request):
    query = request.GET['search_value']
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    context = {'books':books}
    return render(request, "books.html", context)