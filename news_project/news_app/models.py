from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



CATEGORIES = (
        ('IT', 'IT Новости'),
        ('HL', 'Здоровье'),
        ('RS', 'Отдых и досуг'),
    )


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание статьи')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')

    def get_absolute_url(self):
        return f'/news/{self.id}/'
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статьи на сайте'
        verbose_name_plural = 'Статьи на сайте'
        ordering = ['-date_published']
    
class Category(models.Model):
    name = models.CharField(max_length=2, choices=CATEGORIES, blank=False, default='IT')
    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return dict(CATEGORIES)[self.name]
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


