from django.shortcuts import render
from productsapp.models import ProductСollection, ProductProizvoditel

# Create your views here.
def index(request):
	products_sale = ProductСollection.objects.filter(available=True).filter(sale=True)[:6]
	products_novinka = ProductСollection.objects.filter(available=True).filter(novinka=True)[:6]
	proizvoditels = ProductProizvoditel.objects.all()
	return render(request, 'mainapp/index.html', locals())

def company(request):
	return render(request, 'mainapp/about.html')

def contacti(request):
	return render(request, 'mainapp/contact.html')

def shipping(request):
	return render(request, 'mainapp/ship-and-pay.html')