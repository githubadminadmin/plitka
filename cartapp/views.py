from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_POST
from productsapp.models import Product
from .cart import Cart
from django.http import JsonResponse
from django.template.loader import render_to_string

@require_POST
def CartAdd(request, slug, quantity=1, update_quantity = False):
	cart = Cart(request)
	product = get_object_or_404(Product, slug=slug)
	#form = CartAddProductForm(request.POST)
	#if form.is_valid():
	#cd = form.cleaned_data
	token = request.POST.get('csrfmiddlewaretoken', '')
	if request.method == 'POST':
		try:
			quantity = int(request.POST.get('quantity', ''))
		except ValueError:
			quantity = 1
		try:
			update_quantity = request.POST.get('update', '')
		except KeyError:
			update_quantity = False

	edit_quantity = True
	if request.is_ajax():
		if quantity <= 0:
			cart.remove(product)
			cart_header = render_to_string('includes/header_cart_items.html', locals())
			cart_body = render_to_string('cartapp/includes/cart_item_detail.html', locals())
						
			return JsonResponse({'cart_header' : cart_header, 'cart_body' : cart_body})
		else:	
			cart.add(product=product, quantity=quantity, update_quantity=update_quantity)				
			cart_header = render_to_string('includes/header_cart_items.html', locals())		
			cart_body = render_to_string('cartapp/includes/cart_item_detail.html', locals())
			
			return JsonResponse({'cart_header' : cart_header, 'cart_body' : cart_body})
	return render(request, 'cartapp/cart.html', locals())

def CartRemove(request, slug):
	cart = Cart(request)
	product = get_object_or_404(Product, slug=slug)
	edit_quantity = True
	token = request.POST.get('csrfmiddlewaretoken', '')
	if request.is_ajax():
		cart.remove(product)
		cart_header = render_to_string('includes/header_cart_items.html', locals())		
		cart_body = render_to_string('cartapp/includes/cart_item_detail.html', locals())
		return JsonResponse({'cart_header' : cart_header, 'cart_body' : cart_body})#
	
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def CartDetail(request):
	cart = Cart(request)
	return render(request, 'cartapp/cart.html', locals())