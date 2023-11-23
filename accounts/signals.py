import time
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

user_model = get_user_model()


@receiver(signal=post_save, sender=user_model)
def send_email(sender, instance, created, **kwargs):
    """При создании пользователя отправляет письмо"""
    if created:
        from .tasks import send_welcome_email
        time.sleep(5)
        send_welcome_email.delay(instance.pk)
