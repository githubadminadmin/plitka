from django import template
from django.template.loader import render_to_string


register = template.Library()

def count_del(value, arg):
	val = []
	num = ''
	products = []
	for v in value:
		val.append(v.name)

	for i, v in enumerate(val):
		if str(v) == str(arg):
			num = i
			if num % 4 == 0:
				if num >0:
					try:
						products.append(value[num+1])
					except:
						continue
					try:
						products.append(value[num+2])
					except:
						continue
					try:
						products.append(value[num+3])
					except:
						continue
					try:
						products.append(value[num+4])
					except:
						continue
					try:
						products.append(value[num+5])
					except:
						continue
				else:
					products.append(value[num])
					try:
						products.append(value[num+1])
					except:
						continue
					try:
						products.append(value[num+2])
					except:
						continue
					try:
						products.append(value[num+3])
					except:
						continue
					try:
						products.append(value[num+4])
					except:
						continue
		if len(products) > 0:
			render_rezult = render_to_string('productsapp/includes/another_tovar.html', locals())
			if render_rezult:
				return render_rezult
	return ''

register.filter('count_del',count_del)
