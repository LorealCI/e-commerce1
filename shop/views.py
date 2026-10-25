from django.shortcuts import render

# Create your views here.
from .models import Product

def product_list(request):
    # Fetch all products from the database
    products = Product.objects.all()
    # Send the products to the HTML template for rendering
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    # Fetch the product with the given ID from the database
    product = get_object_or_404(Product, pk=pk)
    # Send the product to the HTML template for rendering
    return render(request, 'shop/product_detail.html', {'product': product})