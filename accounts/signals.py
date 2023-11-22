from .models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_welcome_email


@receiver(signal=post_save, sender=User)
def send_email(sender, instance, created, **kwargs):
    if created:
        send_welcome_email.delay(instance.pk)

