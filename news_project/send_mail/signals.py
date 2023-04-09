from django.db.models.signals import post_save
from django.dispatch import receiver
from news_app.models import Article
from django.core.mail import send_mail

@receiver(post_save, sender=Article)
def send_email_to_subscribers(**kwargs):
    instance = kwargs['instance']
    subscribers = instance.cat.subscribers.all()
    text = instance.content[:50]
    for subscriber in subscribers:
        user = subscriber.username
        email = subscriber.email
        send_mail( 
            subject = f'Здравствуй, {user}! Новая статья в твоём любимом разделе!',
            message = text,
            from_email = 'golubev5ergei@yandex.ru',
            recipient_list = [email],
        )