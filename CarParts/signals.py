from django import forms

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def send_successfull_registration_email(user):
    send_mail(
        subject='Registration',
        message='You have been successfully registered',
        from_email='info@carshop.com',
        recipient_list='jdmirchev@gmail.com',
    )


@receiver(post_save, sender=UserModel)
def user_created(*args, **kwargs):
    send_successfull_registration_email(None)
