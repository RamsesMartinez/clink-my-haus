import datetime

from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail


@csrf_protect
def email_contact(request):
    if request.method == 'POST':
        subject = 'Contacto Clink My Haus'
        from_email = request.POST['email']
        to_email = 'test@yopmail.com'
        text_content = request.POST['message']
        send_mail(
            subject,
            text_content,
            from_email,
            [to_email, ],
            fail_silently=False,
        )
    return redirect('projects:list')
