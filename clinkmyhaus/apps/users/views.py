from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from config.settings.base import EMAIL_CONTACT


@csrf_protect
def email_contact(request):
    if request.method == 'POST':
        subject = 'Contacto Clink My Haus'
        from_email = request.POST['email']
        message = request.POST['message']
        name = request.POST['name']
        phone = request.POST['phone']
        text_content = "{} \n\n{}\n{}".format(message, name, phone)
        to_email = EMAIL_CONTACT

        send_mail(
            subject,
            text_content,
            from_email,
            [to_email, ],
            fail_silently=False,
        )
    return redirect('projects:list')
