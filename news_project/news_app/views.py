from django.shortcuts import render, get_object_or_404
from .models import Article

def news_list(request):
    articles = Article.objects.order_by('-date_published')
    return render(request, 'news_app/news_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'news_app/article.html', {'article': article})

def home(request):
    return render(request, 'news_app/home.html')

def about(request):
    return render(request, 'news_app/about.html')

def contacts(request):
    return render(request, 'news_app/contacts.html')