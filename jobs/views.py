from django.shortcuts import render
from .models import Contact
from .models import Job
from django.http import HttpResponse

def home (request):
    jobs = Job.objects
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        messagetitle = request.POST.get('messagetitle')
        subject = request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.messagetitle=messagetitle
        contact.subject=subject
        contact.save()
        return HttpResponse('<h1>Thanks for contact!</h1>')
    return render (request, 'jobs/home.html', {'jobs':jobs})
