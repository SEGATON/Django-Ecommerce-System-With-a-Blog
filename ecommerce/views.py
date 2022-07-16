from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Product, Category

from django.views import generic















def browse_products(request):

	products = Product.objects.all()

	return render(request, 'ecommerce/browse_products.html', 
		{
			'products':products,  
		})



def single_product(request, product):

	single_product = get_object_or_404(Product, slug=product, status='published')
	
	return render(request, 'ecommerce/single_product.html',  
		{
			'single_product': single_product
		})


def cart(request): 

	return render(request, 'ecommerce/cart.html', {
		})



def checkout(request): 
	return render(request, 'ecommerce/checkout.html', {
		
		})








	