from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def send_message(request):
    myinfo = Info.objects.first()
    if request.method == "POST":
        subject = request.POST['subject']
        # name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        '''
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
        '''
        # test, I hope this email finds you
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )

    return render(request, 'contact/contact.html', {'myinfo':myinfo})
