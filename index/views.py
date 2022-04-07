# from django.shortcuts import render
# from django.http import HttpResponse
import os
from .models import repo , certificate
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.

def index(request):
    repos = repo.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
        body = {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['message'],
        }
        message = "\n".join(body.values())

        try:
            send_mail(subject, message, 'webportfolio7@gmail.com', ['mrdlchaturvedi@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        # return redirect("")
        
       
     


    form = ContactForm()
    
    return render(request,'index/index.html',{'repos':repos});




def certifi(request):
    
    certs = certificate.objects.all()
    
    return render(request,'index/certificates.html',{'certs':certs});
    






#
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = "Website Inquiry"
#         body = {
#             'name': form.cleaned_data['name'],
#             'email': form.cleaned_data['email'],
#             'message': form.cleaned_data['message'],
#         }
#         message = "\n".join(body.values())
#
#         try:
#             send_mail(subject, message, 'mdulchat@gmail.com', ['mrdlchaturvedi@gmail.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return redirect("index/index.html")



    # form = ContactForm()
    # return render(request, "index/index.html", {'form': form});