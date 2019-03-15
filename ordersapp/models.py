from django.db import models
from productsapp.models import Product
import hashlib
import uuid

# Create your models here.
STATUCI = (
	('Создан', 'Создан'),
	('Принят', 'Принят'),
	('Завершен', 'Завершен')
)


DELIVERYS = (
	('Самовывоз' , 'Самовывоз'),
	('Доставка' , 'Доставка'),
)


PAYMENTS = (
	('Оплата при доставке', 'Оплата при доставке'),
	('Оплата на сайте', 'Оплата на сайте'),
)


# Create your models here.
class Order(models.Model):
	name = models.CharField(verbose_name='Имя', max_length=50)
	familiya = models.CharField(verbose_name='Фамилия', max_length=50)
	otchestvo = models.CharField(verbose_name='Отчество', max_length=50)
	phone = models.CharField(verbose_name='Телефон', max_length=18)
	email = models.EmailField(verbose_name='Email')
	address =  models.CharField(blank=True, null=True, verbose_name='Адрес', max_length=250)
	comment = models.TextField(verbose_name='Примечание', blank=True, null=True)
	created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
	updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
	status = models.CharField(choices = STATUCI, max_length=20, verbose_name='Статус заказа', default='Создан')
	delivery = models.CharField(choices = DELIVERYS, max_length=20, verbose_name='Тип доставки')
	payment = models.CharField(choices = PAYMENTS, max_length=30, verbose_name='Тип оплаты')
	paid = models.BooleanField(verbose_name='Оплачен', default=False)
	id_order = models.CharField(max_length=40, verbose_name='id заказа', blank=True)

	class Meta:
		ordering = ('-created', )
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

	def __str__(self):
		return 'Заказ: {}'.format(self.id)

	def get_total_cost(self):
		if self.delivery == 'Доставка' and  sum(item.get_cost() for item in self.items.all()) < 10000:
			return sum(item.get_cost() for item in self.items.all()) + 1000
		else:
			return sum(item.get_cost() for item in self.items.all())

	def save(self, *args, **kwargs):
		self.id_order = uuid.uuid4()
		super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
	price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity