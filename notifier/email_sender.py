from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_email(subject, body, recipient):

    email = EmailMultiAlternatives(
        subject=subject,
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[recipient]
    )

    email.attach_alternative(body, "text/html")

    email.send()