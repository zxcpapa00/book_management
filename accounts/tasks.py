from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from book_management.celery import app


@app.task
def send_welcome_email(user_id):
    """Таск для отправки приветственного письма"""
    user_model = get_user_model()
    try:
        user = user_model.objects.get(pk=user_id)
        send_mail(
            subject='Приветственное письмо',
            message='Добро пожаловать на наш сайт',
            from_email='krasnoperoveg2001@yandex.ru',
            recipient_list=[user.email],
            fail_silently=False
        )
    except user_model.DoesNotExist:
        print("Tried to send email to non-existing user '%s'" % user_id)
