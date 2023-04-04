from django.shortcuts import render,redirect
from django.http import HttpResponse


import uuid
from .models import URL
import re
def home(request):
    return render(request,"app/home.html")


def Create(request):
    if request.method == 'POST':
        url=request.POST['link']
        uuid_id=str(uuid.uuid4())[:4]
        new_url=URL.objects.create(link=url,uiid=uuid_id)




        return HttpResponse(uuid_id)


def go_func(request,pk):
    get_url=URL.objects.get(uiid=pk)
    return redirect('http://'+get_url.link)



# Create your views here.
