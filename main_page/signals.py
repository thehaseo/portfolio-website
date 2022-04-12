from django.core.mail import send_mail
from django.conf import settings


def message_notification(sender, **kwargs):
    send_mail(
        'New message recieved',
        'You have recieved a new message in your portfolio website',
        settings.EMAIL_HOST_USER,
        ['gregoriazuaje04@gmail.com',],
        fail_silently = False
    )

