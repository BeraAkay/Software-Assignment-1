from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import *
from .models import *

def entries(request):
    try:
        x=request.path
        x=x.split("/")
        x=int(x[len(x)-1])
        entry = titles[x]
        return render_to_response('template.html',{'entry':entry[0],'desc':entry[1]})
    except:
        raise Http404('Wrong Page Index, please try between 0 and '+str(titleamount-1))

def allentries(request):
    entries = titles
    return render(request,'all.html',{'entries':entries})

def home(request):
    return render(request,'home.html')