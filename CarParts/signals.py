from django import forms

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from CarParts.email_utils import *


UserModel = get_user_model()

def send_successfull_registration_email(user):

    # html_message = render_to_string('email_greetings.html', {'user': user})
    #
    # plain_message = strip_tags(html_message)
    #
    # send_mail(
    #     subject='Registration greetings!',
    #     message='You have been successfully registered',
    #     from_email='info@carshop.com',
    #     recipient_list='jdmirchev@gmail.com',
    # )

    context = {
        'user': user,
    }

    send_email_with_template(
        subject='Registration greetings!',
        template_name='email_greetings.html',
        context=context,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = (user.email, ),
    )


@receiver(post_save, sender=UserModel)
def user_created(*args, **kwargs):
    send_successfull_registration_email(None)
