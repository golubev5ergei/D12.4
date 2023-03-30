from django.forms import ModelForm, TextInput, Textarea
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Заголовок статьи'
            }),
            'content': Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Текст статьи'
            })
        }
