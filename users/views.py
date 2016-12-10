from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User
# Create your views here.

def signup(request):

    if request.method == "POST":
        User.objects.create_user(username=request.POST.get("username"),
                            password=request.POST.get("password"))
        #return render(request,"redirect.html",{"username" : request.POST.get("username")})
        return HttpResponse('<meta http-equiv="refresh" content="0; url=/users/login" />')

    return render(request, "register.html")

