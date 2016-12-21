from django.conf.urls import url
from .models import *
import views


urlpatterns = [
    url(r'entries/$', views.allentries),
    url(r'entries/\d', views.entries),
]
