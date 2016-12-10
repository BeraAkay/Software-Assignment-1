from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=220)
    description = models.CharField(max_length=520)
    '''
kek = "Lorem Ipsum Dolor Sit Amet"
titl = kek.split(" ")
titleamount = len(titl)
titles = list()
for i in range(titleamount):
    titles.append((titl[i], kek))

for n, d in titles:
    Blog.objects.create(name=n, description=d)
'''