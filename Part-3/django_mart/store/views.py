from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from django.core.paginator import Paginator
# Create your views here.

def store(request, category_slug=None):
    if category_slug : 
        category = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(is_available = True, category=category) # category wise products
        page = request.GET.get('page')
        print(page)
        paginator = Paginator(products, 1) # Paginator(objects, per page e kotogula product dekhte chai)
        paged_product = paginator.get_page(page)
    else : 
        products = Product.objects.filter(is_available = True) # all products
        paginator = Paginator(products, 2) # Paginator(objects, per page e kotogula product dekhte chai)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        # print(paged_product)
        for i in paged_product:
            print(i)
        print(paged_product.has_next(), paged_product.has_previous(), paged_product.previous_page_number, paged_product.next_page_number)
        
    categories = Category.objects.all()
    context = {'products' : paged_product, 'categories' : categories, }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(slug = product_slug, category__slug = category_slug)
    print('single product ', single_product)
    
    return render(request, 'store/product-detail.html', {'product' : single_product})