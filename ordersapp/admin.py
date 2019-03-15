from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_field = ['product']

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'name',  'familiya', 'phone', 'status', 'delivery', 'payment', 'comment', 'paid', 'created']
	list_filter = ['paid', 'created', 'status', 'delivery', 'payment']
	exclude = ['id_order']
	inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)