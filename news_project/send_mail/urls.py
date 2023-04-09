from django.urls import path
from .views import subscribe, sub_test

urlpatterns = [
    path('<str:category_name>', sub_test, name='subscribe'),
]