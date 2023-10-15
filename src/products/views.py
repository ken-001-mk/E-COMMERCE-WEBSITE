from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from django.db.models import Q
from .forms import NewProductForm, EditProductForm

def browse(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    browse = Product.objects.filter(is_sold=False)

    if category_id:
        browse = browse.filter(category_id=category_id)

    if query:
        browse = browse.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'products/browse.html', {
        'browse': browse,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })

def info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(
        category=product.category, is_sold=False
    ).exclude(pk=pk)[0:5]

    return render(request, 'products/info.html', {
        'product': product,
        'related_products': related_products,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()

            return redirect('products:info', pk=product.pk)
        
    else:
        form = NewProductForm()

    return render(request, 'products/form.html', {
        'form': form,
        'title': 'New Product',
    })

@login_required
def edit(request, pk):
    products = get_object_or_404(Product, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=products)

        if form.is_valid():
            form.save()

            return redirect('products:info', pk=products.id)
        
    else:
        form = EditProductForm(instance=products)

    return render(request, 'products/form.html', {
        'form': form,
        'title': 'Edit Product',
    })

@login_required
def delete(request, pk):
    products = get_object_or_404(Product, pk=pk, created_by=request.user)
    products.delete()

    return redirect('dashboard:index')

