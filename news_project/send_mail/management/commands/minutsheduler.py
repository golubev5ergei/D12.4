from datetime import datetime, timedelta
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from news_app.models import Article, Category
from apscheduler.schedulers.background import BackgroundScheduler

# Функция для проверки новых статей во всех категориях
def check_new_articles_all_categories():
    # Получение текущей даты и времени
    now = datetime.now()

    # Вычисление времени, за последние 1 минуту от текущей даты и времени
    one_minute_ago = now - timedelta(minutes=1)

    # Получение всех категорий
    categories = Category.objects.all()

    # Перебор всех категорий
    for category in categories:
        # Получение всех статей в текущей категории, созданных за последнюю минуту
        new_articles = Article.objects.filter(category=category, created_at__gte=one_minute_ago)

        # Если есть новые статьи
        if new_articles:
            subscribers = category.subscribers.all()
            text = new_articles[0].content[:50]  # Пример текста статьи, можно изменить на нужный формат
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
                    subject=f'{user}, Новая статья в категории {category_name}',
                    body='',
                    from_email='testmail@test.com',
                    to=[email,]
                )
                msg.attach_alternative(html, 'text/html')
                try:
                    msg.send()
                except Exception as e:
                    print(e)

# Создание и настройка планировщика задач
scheduler = BackgroundScheduler()
scheduler.add_job(check_new_articles_all_categories, 'interval', minutes=1)  # Выполнение каждую минуту
scheduler.start()
