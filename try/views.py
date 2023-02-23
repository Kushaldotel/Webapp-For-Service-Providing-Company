from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Direct, Blog
# Create your views here.
def home(request):
    if request.method=="POST":
        number = request.POST.get('number')
        if not number:
            messages.add_message(request,messages.INFO, 'Fill the number field.')
            return render(request,'try/index.html')

        data = Direct.objects.create(number=number)
        # data.save()
        return redirect('home')
    return render(request,'try/index.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('Name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        message= request.POST.get('message')
        contact= Contact(Name=name, number=number, email=email, message=message)
        contact.save()        
        return redirect('contact')
    return render(request, 'try/contacts.html')

def about(request):
    return render(request, 'try/pricing.html')

def services(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'try/integrations.html', context)

def blog(request):
    return render(request, 'try/features.html')


def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}
    return render(request, 'try/blogpost.html', context)
