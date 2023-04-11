from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from news_app.models import Article
from news_app.tasks import article_add_sub


@receiver(post_save, sender=Article)
def notify_subscribers(sender, instance, **kwargs):
    print(kwargs)
    if kwargs['created']:
        article_add_sub(instance)
    