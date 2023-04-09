from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ArticleList.as_view(), name='news'),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('<int:pk>', views.ArticleDetail.as_view(), name='article-detail'),
    path('<int:pk>/update', views.ArticleUpdate.as_view(), name='article-update'),
    path('<int:pk>/delete', views.ArticleDelete.as_view(), name='article-delete'),
    path('create', views.ArticleCreate.as_view(), name='create'),
    path('protect/', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('news/<str:category>/', views.ArticleList.as_view(), name='news_category'),
    path('subscribe/', include('send_mail.urls')),
]