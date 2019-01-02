from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.conf import settings
from django.utils import timezone

email_address = settings.EMAIL_HOST_USER

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data.get('name')
            subject = form.cleaned_data.get('subject')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            
            try:
                message_final = "From: {}\nReceived on {}\nMessage:\n{}".format(name,timezone.now().date(), message)
                send_mail(subject, message_final, email, [email_address])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact-success')
            
    return render(request, "sendemail/email.html", {'form': form})

def successView(request):
    # return HttpResponse('Success! Thank you for your message.')
    return render(request, "sendemail/success.html")

