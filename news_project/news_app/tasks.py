from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


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
            'post': text,
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
        
