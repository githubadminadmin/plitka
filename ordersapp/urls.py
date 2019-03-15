from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.order_create, name='order_create'),
	path('created/<int:id>/<str:id_order>', views.created, name='created'),
]