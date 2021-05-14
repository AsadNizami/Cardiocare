from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from project.settings import EMAIL_HOST_USER

def test_report(request):
    body = 'template/app/email.html'
    message = EmailMultiAlternatives(
        subject='Test Report Ready',
        body=body,
        from_email=EMAIL_HOST_USER,
        to=[request.user.email]
    )
    html_template = render_to_string('app/email.html', {'data': request.user})
    message.attach_alternative(html_template, 'text/html')
    message.send()

def join_mail(email):
    body = 'template/app/join_email.html'
    message = EmailMultiAlternatives(
        subject='Welcome!',
        body=body,
        from_email=EMAIL_HOST_USER,
        to=[email]
    )
    html_template = render_to_string('app/join_email.html')
    message.attach_alternative(html_template, 'text/html')
    message.send()


