from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout

from products.models import Product, Category
from .forms import SignupForm, LogoutForm

def index(request):
    products = Product.objects.filter(is_sold=False)[0:7]
    categories = Category.objects.all()
    return render(request, 'shoppers/index.html', {
        'products': products,
        'categories': categories
    })

def follow_us(request):
    return render(request, 'shoppers/follow_us.html')

def terms(request):
    return render(request, 'shoppers/terms.html')

def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = request.POST['email']
        send_mail(subject, message, from_email, [''])
        return HttpResponseRedirect('/contact/')
    return render(request, 'shoppers/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'shoppers/signup.html', {
        'form': form
    })

def user_logout(request):
    form = LogoutForm()

    if request.method == 'POST':
        form = LogoutForm(request.POST)
        if form.is_valid():
            auth_logout(request)
            return redirect('/login/')

    return render(request, 'shoppers/logout.html', {
        'form': form
    })