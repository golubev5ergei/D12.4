from django_filters import FilterSet
from .models import Article


class ArticleFilter(FilterSet):
    class Meta:
        model = Article
        fields = ('cat', 'date_published')