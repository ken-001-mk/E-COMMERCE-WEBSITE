from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product

@login_required
def index(request):
    products = Product.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'products': products,
    })

