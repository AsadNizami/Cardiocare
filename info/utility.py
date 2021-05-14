from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from project.settings import EMAIL_HOST_USER


def invite_mail(request, email):
    body = 'template/info/invite.html'
    message = EmailMultiAlternatives(
        subject='Invitation for a free test at cardiocare!',
        body=body,
        from_email=EMAIL_HOST_USER,
        to=[email]
    )
    html_template = render_to_string('info/invite.html', {'data': request.user})
    message.attach_alternative(html_template, 'text/html')
    message.send()
