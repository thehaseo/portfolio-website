from django.apps import AppConfig
from django.db.models.signals import post_save



class MainPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_page'

    def ready(self):
        from . import signals
        from .models import RecievedMessages
        post_save.connect(signals.message_notification, RecievedMessages)
