# from django.shortcuts import render
# from django.http import HttpResponse
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
        
       
            # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/downloadapp/Files/' + 'MridulsResume.pdf'
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % 'MridulsResume.pdf'
        # Return the response value


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