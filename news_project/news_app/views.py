from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from .filters import ArticleFilter
from django.contrib.auth.mixins import LoginRequiredMixin



def news_list(request):
    articles = Article.objects.order_by('-date_published')
    return render(request, 'news_app/news_list.html', {'articles': articles})
    

class ArticleList(ListView):
    model = Article
    template_name = 'news_app/news_list.html'
    context_object_name = 'articles'
    ordering = ['-date_published']
    paginate_by = 5

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['filter'] = ArticleFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'news_app/article.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            is_author = user.groups.filter(name='authors').exists()
            context['is_author'] = is_author
        return context


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'news_app/create.html'
    form_class = ArticleForm
    success_url = '/news/'


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'news_app/delete.html'
    success_url = '/news/'


class ArticleCreate(LoginRequiredMixin, CreateView):
    template_name = 'news_app/create.html'
    form_class = ArticleForm
    success_url = '/news/'

def home(request):
    return render(request, 'news_app/home.html')


def about(request):
    return render(request, 'news_app/about.html')


def contacts(request):
    return render(request, 'news_app/contacts.html')

def reg(request):
    return render(request, 'protect/index.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else: error = 'Ошибка заполнения формы'
    form = ArticleForm()
    data = {
        'form': form,
        'error': error 
    }
    return render(request, 'news_app/create.html', data)