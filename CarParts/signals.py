# from django import forms
#
# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth import get_user_model
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# from django.conf import settings
# from CarParts.email_utils import *
#
#
# UserModel = get_user_model()
#
# def send_successfull_registration_email(user):
#
#     context = {
#         'user': user,
#     }
#
#     send_email_with_template(
#         subject='Registration greetings!',
#         template_name='email_greetings.html',
#         context=context,
#         from_email = settings.EMAIL_HOST_USER,
#         recipient_list = (user.email, ),
#     )
#
#
# # @receiver(post_save, sender=UserModel)
# # def user_created(*args, **kwargs):
# #     send_successfull_registration_email(None)
