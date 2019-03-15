from django.shortcuts import render, get_object_or_404
from .models import Product, ProductProizvoditel, ProductСollection, ProductCategory, CompositionsCollection
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def catalog(request):
	products = Product.objects.all()
	return render(request, 'productsapp/catalog.html', locals())

def category(request, cat):
	cat = cat
	if cat:
		cat_name = ProductCategory.objects.get(slug=cat)

	collections = ProductСollection.objects.filter(productcategory__slug=cat).filter(available=True)

	proizvodit_filters = []
	collect_filters = []

	for collection in collections:
		pr_f = [collection.productproizvoditel.id, collection.productproizvoditel.name, collection.productproizvoditel.slug]
		if pr_f not in proizvodit_filters:
			proizvodit_filters.append(pr_f)

		cl_f = [collection.id, collection.name, collection.slug]
		if cl_f not in collect_filters:
			collect_filters.append(cl_f)
	pr_f_ch = []
	cl_f_ch = []
	if request.is_ajax():
			
		try:
			if request.GET['pr']:
				pr_f_ch = request.GET.getlist('pr')
				pr_ch = request.GET.getlist('pr', '')
				for i, item in enumerate(pr_ch):
				    pr_ch[i] = int(item)
		except:
			for pr_f in proizvodit_filters:
				pr_f_ch.append(pr_f[0])

		
		try:
			if request.GET['cl']:
				cl_f_ch = request.GET.getlist('cl', '')
				cl_ch = request.GET.getlist('cl', '')
				for i, item in enumerate(cl_ch):
				    cl_ch[i] = int(item)
		except:
			for cl_f in collect_filters:
				print('rere')
				cl_f_ch.append(cl_f[0])


		products_collect = ProductСollection.objects.filter(Q(productcategory__slug=cat) & Q(productproizvoditel__in=pr_f_ch) & Q(id__in=cl_f_ch))
		collections = ProductСollection.objects.filter(Q(productcategory__slug=cat) & Q(productproizvoditel__in=pr_f_ch) & Q(id__in=cl_f_ch))

		pr_f_new = []
		cl_f_new = []	

		for collection in collections:
			if 'pr' not in request.GET:
				proizvodit_filters.clear()	
				pr_f = [collection.productproizvoditel.id, collection.productproizvoditel.name, collection.productproizvoditel.slug]		
				if pr_f not in pr_f_new:
					pr_f_new.append(pr_f)
			else:
				proizvodit_filters.clear()
				collections_collect = ProductСollection.objects.filter(Q(productcategory__slug=cat) & Q(id__in=cl_f_ch))				
				for collect_collect in collections_collect:
					pr_f = [collect_collect.productproizvoditel.id, collect_collect.productproizvoditel.name, collect_collect.productproizvoditel.slug]
					if pr_f not in pr_f_new:
						pr_f_new.append(pr_f)
			
			if ('cl' not in request.GET):		
				collect_filters.clear()	
				cl_f = [collection.id, collection.name, collection.slug]
				if cl_f not in cl_f_new:
					cl_f_new.append(cl_f)
			else:
				collect_filters.clear()
				collections_proizvod = ProductСollection.objects.filter(Q(productcategory__slug=cat) & Q(productproizvoditel__in=pr_f_ch))				
				for collect_proizvod in collections_proizvod:
					cl_f = [collect_proizvod.id, collect_proizvod.name, collect_proizvod.slug]
					if cl_f not in cl_f_new:
						cl_f_new.append(cl_f)
			
		if len(cl_f_new) > 0:
			collect_filters = cl_f_new			

		if len(pr_f_new) > 0:
			proizvodit_filters = pr_f_new	

		filter_setting = render_to_string('productsapp/includes/filterbar.html', locals())
		product_view = render_to_string('productsapp/includes/collection.html', locals())
		return JsonResponse({'filter_setting':filter_setting, 'product_view':product_view})#'filter_setting':filter_setting, 'url':url[:-1],


			
	try:
		page_num = request.GET['page']
	except KeyError:
		page_num = 1


	paginator = Paginator(ProductСollection.objects.filter(productcategory__slug=cat).filter(available=True) , 8)

	try:
		products_collect = paginator.page(page_num)
	except InvalidPage:
		products_collect = paginator.page(1)

	return render(request, 'productsapp/catalog.html', locals())


def collect_product(request, cat, collect):
	collect_name = ProductСollection.objects.get(slug=collect)
	if cat:
		cat_name = ProductCategory.objects.get(slug=cat)
	products = Product.objects.filter(Q(category__slug=cat) & Q(collection__slug=collect))
	compositionscollection = CompositionsCollection.objects.filter(collection=collect_name.id)
	return render(request, 'productsapp/catalog.html', locals())

def product(request, cat, collect, product):
	cat = cat
	collect = collect
	product = get_object_or_404(Product, slug=product)
	products = Product.objects.filter(Q(category__slug=cat) & Q(collection__slug=collect))
	return render(request, 'productsapp/product.html', locals())