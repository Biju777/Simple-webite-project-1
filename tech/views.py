from django.shortcuts import render, HttpResponse
from tech.models import Contact, Service, Blog
from django.contrib import messages


def index(request):
    blogs = Blog.objects.all()
    service = Service.objects.all()
    context = {"blogs":blogs, "service":service}
    return render(request, "index.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        mesage = request.POST['mesage']
        contacts = Contact(name=name, email=email, number=number, mesage=mesage)
        messages.success(request, "Your form has been submit successfully.")
        contacts.save()
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def services(request):
    service = Service.objects.all()
    return render(request, "service.html", {
        'service': service
    })


