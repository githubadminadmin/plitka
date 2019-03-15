from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cartapp.cart import Cart
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import hashlib
from django.db.models import Q

# Create your views here.
def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = Order()
			#order.id_user = request.user
			order.name = form.cleaned_data['name']
			order.familiya = form.cleaned_data['familiya']
			order.otchestvo = form.cleaned_data['otchestvo']
			order.phone = form.cleaned_data['phone']
			order.email = form.cleaned_data['email']
			order.address = form.cleaned_data['address']
			order.comment = form.cleaned_data['comment']
			order.delivery = form.cleaned_data['delivery']
			order.payment = form.cleaned_data['payment']
			order.save()
			for item in cart:
				OrderItem.objects.create(order=order, 
										 product=item['product'],
										 price=item['price'],
										 quantity=item['quantity'])
			cart.clear()
			url = '/order/created/' + str(order.id) + '/' + str(order.id_order) 
			email_content = {'url': 'http://kamen-plitka.ru'+url, 'id':order.id, 'name':order.name}
			subject = 'Заказ на сайте kamen-plitka.ru'
			message_html = render_to_string('ordersapp/email/email_order.html', email_content)
			sender = 'sales@kamen-plitka.ru'
			recipients = [form.cleaned_data['email']]
			msg = EmailMultiAlternatives(subject, message_html, sender, recipients)
			msg.attach_alternative(message_html, "text/html")
			msg.send()
			return redirect(url)
			return render(request, 'orders/order.html', locals())
			

	form = OrderCreateForm()
	return render(request, 'ordersapp/checkout.html', locals())

def created(request, id, id_order):
	order = get_object_or_404(Order, id_order=id_order, id=id)
#	if order:
#		if order.id_user == request.user:
#			print(order.id_user, request.user)
#			order_user_id = order.id_user
	return render(request, 'ordersapp/order.html', locals())