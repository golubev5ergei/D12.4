from django.core.mail import send_mail

def article_add_sub(instance):
    subscribers = instance.cat.subscribers.all()
    text = instance.content[:50]
    for subscriber in subscribers:
        user = subscriber.username
        email = subscriber.email
        send_mail( 
            subject = f'Здравствуй, {user}! Новая статья в твоём любимом разделе!',
            message = text,
            from_email = 'test@test.com',
            recipient_list = [email,],
        )
