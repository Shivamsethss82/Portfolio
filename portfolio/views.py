from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Contact

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        c_name = request.POST.get('name')
        c_email = request.POST.get('email')
        c_phoneno = request.POST.get('num')
        c_desc = request.POST.get('desc')
        queryy = Contact(name=c_name, email=c_email,phonenumber=c_phoneno, description=c_desc)
        queryy.save()
        messages.success(request, "Thanks for contact with us")

        return redirect('/contact')
    return render(request, 'contact.html')