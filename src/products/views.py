from django.shortcuts import render , get_object_or_404
from .models import Category , Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator




def index(request):
    q = request.GET.get('q')
    categories = Category.objects.all()
    if q :
        products = Product.objects.filter(available=True , category__slug=q)
        paginator = Paginator(products , 25)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)
    else:
        products = Product.objects.filter(available=True)
        paginator = Paginator(products , 25)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)
    cart_product_form = CartAddProductForm()
    context = {'categories':categories ,'products':products,'cart_product_form':cart_product_form}
    return render(request , 'products/index.html' , context)



def product_detail(request , product_slug , cat_slug=None ):
    product = get_object_or_404(Product , slug=product_slug)
    cart_product_form = CartAddProductForm()
    context ={'product':product ,'cart_product_form':cart_product_form}
    return render(request , 'products/product_detail.html' , context)
