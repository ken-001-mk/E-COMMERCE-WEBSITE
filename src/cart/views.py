from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total, 'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product = product.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'Added {product.name} to your cart.')
    except CartItem.DoesNotExist:
        cart_item = CartItem(cart=cart, product=product, quantity=1)
        cart_item.save()
        messages.success(request, f'Added {product.name} to your cart.')
    
    return redirect('cart:view_cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'Removed {product_name} from your cart.')
    return redirect('cart:view_cart')
