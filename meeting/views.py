from django.shortcuts import render , get_object_or_404 , redirect

from .models import Metting , Room
from .forms import MeetingForm




def detail(request, id):
    meeting = get_object_or_404(Metting,pk=id) 
    return render(request , "meeting/detail.html" , {"meeting": meeting})



def roomsinfo(request ):
    return render(request,"meeting/roominfo.html" ,
     {"rooms" : Room.objects.all()})



def new(request):
    if request.method == "POST":
        # form has been submitted, precess data
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome") # welcome here the name of view passed

    else:
        form = MeetingForm()
        
    return render(request , "meeting/new.html", {"form" : form}) # this statment return in tow condetion one if not sub,eted another if not falid data


   

    
