from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    #name = "dop"
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            'message from ' + message_name, #subject
            'message', # message
            'message_emall', # from email
            ['leilla.foundation@gmail.com', 'dopdd@yahoo.com'] # send to ...
        )

        # return user to same page
        return render(request, 'contact.html', {'message_name': message_name})

    else:
            return render(request, 'contact.html', {})

def projects(request):
    return render(request, 'projects.html', {})


def vision(request):
    return render(request, 'vision.html', {})


def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'blog.html', {})


def blog_details(request):
    return render(request, 'blog-details.html', {})

