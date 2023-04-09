from django.apps import AppConfig


class SendMailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'send_mail'

    def ready(self):
        import send_mail.signals
        
