from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


def send_email_with_template(subject, email, recipient_list, template_name, context):
    html_message = render_to_string(template_name, context=context)
    plain_message = strip_tags(html_message)

    return send_mail(
        subject=subject,
        message=plain_message,
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
    )