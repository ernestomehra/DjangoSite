from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):

	if request.method == 'POST':
		message = request.POST['body']
		send_mail(subject, message, 
			settings.EMAIL_HOST_USER, 
			['mehra9090@gmail.com'],
		fail_silently=False)
	return render(request, 'mainsite/home.html')


