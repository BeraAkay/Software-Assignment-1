from django.conf.urls import url
from .models import *
import views


urlpatterns = [
    url(r'entries/$', views.allentries),
    url(r'entries/\d', views.entries),
    url(r'entries/all/$', views.superall),
    url(r'entries/all/user/(?P<userId>[0-9]+)$', views.supersolo),
]
