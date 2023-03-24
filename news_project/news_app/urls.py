from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('news/', views.news_list),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('news/<int:article_id>/', views.article_detail),
]