from django.urls import path
from . import views


urlpatterns = [
	path('', views.catalog, name='catalog'),
	path('<str:cat>', views.category, name='category'),
	path('<str:cat>/<slug:collect>/', views.collect_product, name='collect_product'),
	path('<str:cat>/<slug:collect>/<slug:product>', views.product, name='product')
]