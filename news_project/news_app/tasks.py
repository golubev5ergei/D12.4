from datetime import datetime, timedelta
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from news_app.models import Category, Article


def article_add_sub(instance):
    subscribers = instance.cat.subscribers.all()
    text = instance.content[:50]
    template = 'news_app/new_post.html'
    for subscriber in subscribers:
        user = subscriber.username
        email = subscriber.email
        category = instance.cat.name
        html = render_to_string(
            template_name=template,
            context={
            'category': category,
            'posts': text,
            },
        )
        msg = EmailMultiAlternatives(
            subject=f'Новая статья в категории {category}',
            body='',
            from_email='testmail@test.com',
            to=[email,]
        )
        msg.attach_alternative(html, 'text/html')
        try:
            msg.send()
        except Exception as e:
            print(e)





def check_new_articles(Category):
    now = datetime.now()
    week_ago = now - timedelta(minutes=1)
    new_articles = Article.objects.filter(category=Article.cat, created_at__gte=week_ago)

    return new_articles



def check_new_articles_all_categories():
    now = datetime.now()
    one_minute_ago = now - timedelta(minutes=1)
    categories = Category.objects.all()
    for category in categories:
        new_articles = Article.objects.filter(cat=category, date_published=one_minute_ago)
        if new_articles:
            subscribers = category.subscribers.all()
            text = new_articles[0].content[:50]
            template = 'news_app/new_post.html'
            for subscriber in subscribers:
                user = subscriber.username
                email = subscriber.email
                category_name = category.name
                html = render_to_string(
                    template_name=template,
                    context={
                    'category': category_name,
                    'posts': text,
                    },
                )
                msg = EmailMultiAlternatives(
                    subject=f'Новая статья в категории {category_name}',
                    body='',
                    from_email='testmail@test.com',
                    to=[email,]
                )
                msg.attach_alternative(html, 'text/html')
                try:
                    msg.send()
                except Exception as e:
                    print(e)


