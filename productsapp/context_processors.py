from .models import ProductCategory

def get_category(request):
	categorys = ProductCategory.objects.all()
	return {'categorys': categorys}