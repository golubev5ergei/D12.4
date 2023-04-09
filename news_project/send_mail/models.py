from django.db import models
from news_app.models import Category
from django.contrib.auth.models import User, Group


it_group, created = Group.objects.get_or_create(name='it-sub')
rs_group, created = Group.objects.get_or_create(name='rs-sub')
hl_group, created = Group.objects.get_or_create(name='hl-sub')

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
