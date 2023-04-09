from django.forms import ModelForm, TextInput, Textarea
from .models import Article

class ArticleForm(ModelForm):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'


    class Meta:
        model = Article
        fields = ['title', 'content', 'cat']
        widgets = {
            'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Заголовок статьи'
            }),

            'content': Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Текст статьи'
            }),

        }
