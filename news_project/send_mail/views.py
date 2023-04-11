from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from news_app.models import Category
from django.contrib.auth.models import Group


@login_required
def subscribe(request, category_name):
    user = request.user
    sub_category = category_name.lower()

    if sub_category == 'it':
        it_group = Group.objects.get(name='it-sub')
        it_group.user_set.add(user)
    elif sub_category == 'rs':
        rs_group = Group.objects.get(name='rs-sub')
        rs_group.user_set.add(user)
    elif sub_category == 'hl':
        hl_group = Group.objects.get(name='hl-sub')
        hl_group.user_set.add(user)
    
    user.save()

    print(category_name)
    return redirect('news')


@login_required
def sub_test(request, category_name):
    user = request.user
    category = Category.objects.get(name = category_name)
    category.subscribers.add(user)

    return redirect ('news')

