from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('news/', views.ArticleList.as_view(), name='news'),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('<int:pk>', views.ArticleDetail.as_view(), name='article-detail'),
    path('<int:pk>/update', views.ArticleUpdate.as_view(), name='article-update'),
    path('<int:pk>/delete', views.ArticleDelete.as_view(), name='article-delete'),
    path('create', views.create, name='create'),
]