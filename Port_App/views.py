from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings



def home(request):
    return render(request, 'Port_App/index.html')


def contact_view(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if all([name, email, subject, message]):
            try:
                full_message = f"From: {name} <{email}>\nSubject:\n{subject}\nMessage:\n{message}"
                send_mail(
                    subject,
                    full_message,
                    email,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                context['result'] = '✅ Email sent successfully!'
            except Exception as e:
                context['result'] = f'❌ Error sending email: {e}'
        else:
            context['result'] = '⚠️ All fields are required.'

    return render(request, "Port_App/index.html", context)