from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('o-companii', views.company, name='company'),
	path('contacti', views.contacti, name='contacti'),
	path('shipping-and-payment', views.shipping, name='shipping'),
]