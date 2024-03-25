from django.shortcuts import render
from .models import events as Event
#import get_object_or_404
from django.shortcuts import get_object_or_404
#import login required
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

@login_required(login_url="accounts:login")
def event(request):
    events=Event.objects.all()
    context={'events':events}
    return render(request, "events.html", context)


@login_required(login_url="accounts:login")
def event_detail(request,id):
    event=get_object_or_404(Event, id=id)
    context={'event':event}
    return render(request, "event_detail.html",context)


def search(request):
    quary=request.GET['search_value']
    events=Event.objects.filter(Q(title__icontains=quary) | Q(description__icontains=quary) | Q(location__icontains=quary))
    context={'events':events}
    
    return render(request, "events.html", context)
