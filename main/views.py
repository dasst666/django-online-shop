from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator
from cart.forms import CartAddProductForm

def popular_list(request):
    products = Product.objects.filter(available=True)[:3]
    return render(request, 'main/index/index.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, 
                                slug=slug, 
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 
                'main/product/detail.html', 
                {'product': product, 
                'cart_product_form': cart_product_form})

def product_list(request, category_slug=None):
    page = request.GET.get('page', 1)
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 1)
    current_page = paginator.page(int(page))
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        paginator = Paginator(products.filter(category=category), 1)
        current_page = paginator.page(int(page))
    return render(request, 
                    'main/product/list.html', 
                    {'category': category, 
                    'categories': categories, 
                    'products': current_page,
                    'slug_url': category_slug})


