from django.urls import path
from . import views

urlpatterns = [
	path('', views.CartDetail, name='CartDetail'),
	path('add/<slug:slug>', views.CartAdd, name='CartAdd'),
	path('delete/<slug:slug>', views.CartRemove, name='CartRemove')
] 