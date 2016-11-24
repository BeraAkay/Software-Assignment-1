from __future__ import unicode_literals

from django.db import models

# Create your models here.
kek ="Lorem Ipsum Dolor Sit Amet"
titl=kek.split(" ")
titleamount=len(titl)
titles = list()
for i in range (titleamount):
    titles.append((titl[i],kek))