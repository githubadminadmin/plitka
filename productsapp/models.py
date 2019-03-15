from django.db import models
from django.utils.safestring import mark_safe
from smart_selects.db_fields import ChainedForeignKey
import uuid, os
#from imagekit.models import ImageSpecField
#from imagekit.processors import ResizeToFill

# Create your models here.
class ProductCategory(models.Model):
	name = models.CharField(max_length=100, unique=True, db_index=True,verbose_name='Название категории')
	slug = models.SlugField(max_length=100, unique=True, db_index=True)

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name


class ProductTypeSurface(models.Model):
	name = models.CharField(max_length=100, unique=True, db_index=True,verbose_name='Тип поверхности')
	slug = models.SlugField(max_length=100, unique=True, db_index=True)

	class Meta:
		verbose_name = 'Тип поверхности'
		verbose_name_plural = 'Типы поверхности'

	def __str__(self):
		return self.name


class ProductCountry(models.Model):
	name = models.CharField(max_length=100, unique=True, db_index=True,verbose_name='Страна')
	slug = models.SlugField(max_length=100, unique=True, db_index=True)


	class Meta:
		verbose_name = 'Страна'
		verbose_name_plural = 'Страны'

	def __str__(self):
		return self.name

def get_file_path_proizvoditel(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	return os.path.join('proizvoditel', filename)

class ProductProizvoditel(models.Model):
	productcountry =  models.ForeignKey(ProductCountry, on_delete=models.CASCADE, verbose_name='Страна')
	name = models.CharField(max_length=100, unique=True, db_index=True,verbose_name='Производитель')
	slug = models.SlugField(max_length=100, unique=True, db_index=True)
	image = models.ImageField(upload_to=get_file_path_proizvoditel, blank=True, verbose_name="Логотип производителя")
	description = models.TextField(blank=True, verbose_name="Описание")

	class Meta:
		verbose_name = 'Производитель'
		verbose_name_plural = 'Производители'

	def __str__(self):
		return self.name



class ProductType(models.Model):
	name = models.CharField(max_length=100, unique=True, db_index=True,verbose_name='Тип плитки')
	slug = models.SlugField(max_length=100, unique=True, db_index=True)

	class Meta:
		verbose_name = 'Тип плитки'
		verbose_name_plural = 'Типы плитки'

	def __str__(self):
		return self.name


def get_file_path_collect(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	return os.path.join('collections', filename)

class ProductСollection(models.Model):
	productcategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категория')
	productproizvoditel =  models.ForeignKey(ProductProizvoditel, on_delete=models.CASCADE, verbose_name='Производитель')
	name = models.CharField(max_length=100, unique=True, db_index=True,verbose_name='Коллекция')
	slug = models.SlugField(max_length=100, unique=True, db_index=True)
	image = models.ImageField(upload_to=get_file_path_collect, blank=True, verbose_name="Картинка коллекции")
	description = models.TextField(blank=True, verbose_name="Описание")
	available = models.BooleanField(default=True, verbose_name="Доступна к публикации")	
	novinka = models.BooleanField(default=True, verbose_name="Новинка")
	sale = models.BooleanField(default=True, verbose_name="Распродажа")	
	
	
	class Meta:
		verbose_name = 'Коллекции'
		verbose_name_plural = 'Коллекции'

	def __str__(self):
		return self.name


	def GetCollectName(self):
		return self.name + ' (' + self.productproizvoditel.name + ', ' + self.productproizvoditel.productcountry.name + ')'






	def delete(self, *args, **kwargs):
		self.image.delete(save=False)
		super(ProductСollection, self).delete(*args, **kwargs)
		

class CompositionsCollection(models.Model):
	collection = models.ForeignKey(ProductСollection, related_name='items', on_delete=models.CASCADE)
	name =  models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='Элемент коллекции')

	def __str__(self):
		return self.name.name


	class Meta:
		verbose_name = 'Состав коллекции'
		verbose_name_plural = 'Состав коллекции'


class ProductColor(models.Model):
	name = models.CharField(max_length=100, unique=True, db_index=True,verbose_name='Цвет')
	slug = models.SlugField(max_length=100, unique=True, db_index=True)

	class Meta:
		verbose_name = 'Цвет'
		verbose_name_plural = 'Цвета'

	def __str__(self):
		return self.name


def get_file_path_products(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	return os.path.join('products', filename)


class Product(models.Model):
	article = models.CharField(max_length=10, verbose_name='Артикул')
	category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Категория')
	name = models.CharField(max_length=100, verbose_name='Название')
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to=get_file_path_products, blank=True, verbose_name="Картинка товара")
#	country =  models.ForeignKey(ProductCountry, on_delete=models.CASCADE, verbose_name='Страна')
#	proizvoditel =  ChainedForeignKey(ProductProizvoditel, 
#									  chained_field="country", 
#									  chained_model_field="productcountry", 
#									  show_all=False, 
#									  auto_choose=True, 
#									  sort=True, 
#									  verbose_name='Производитель',
#									  related_name='proizvod')related_name="items"
	collection = ChainedForeignKey(ProductСollection, 
									  chained_field="category", 
									  chained_model_field="productcategory", 
									  show_all=False, 
									  auto_choose=True, 
									  sort=True, 
									  verbose_name='Коллекция')
	copmositions = ChainedForeignKey(CompositionsCollection,
									  chained_field="collection", 
									  chained_model_field="collection", 
									  show_all=False, 
									  auto_choose=True, 
									  sort=True, 
									  #related_name="items", 
									  verbose_name="Входит в состав")
	description = models.TextField(blank=True, verbose_name="Описание")
	price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
	#tip = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='Тип')
	surface = models.ForeignKey(ProductTypeSurface, on_delete=models.CASCADE, verbose_name='Тип поверхности')
	color = models.ForeignKey(ProductColor, on_delete=models.CASCADE, verbose_name='Цвет')
	weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес упаковки, кг', null=True, blank=True)
	height = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Высота, см', null=True, blank=True)
	width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ширина, см', null=True, blank=True)
	col_in_upac =  models.PositiveIntegerField(verbose_name="Кол-во в упаковке", blank=True, null=True)
	area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Площадь в упаковке', null=True, blank=True)
	stock = models.PositiveIntegerField(verbose_name="В наличии шт")
	available = models.BooleanField(default=True, verbose_name="Доступен")
	hits = models.PositiveIntegerField(verbose_name="Количество продаж", default=0, null=True)

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __str__(self):
		return self.name

	def image_img(self):
		if self.image:
			from django.utils.safestring import mark_safe
			return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
		else:
			return '(Нет изображения)'
		image_img.short_description = 'Картинка товара'
		image_img.allow_tags = True


	def save(self, *args, **kwargs):
		if self.width == None:
			self.area = None
		elif self.height == None:
			self.area = None
		elif self.col_in_upac == None:
			self.area = (self.width * self.height * 1) / 10000		
		else:
			self.area = (self.width * self.height * self.col_in_upac) / 10000
		super(Product, self).save(*args, **kwargs)


	def delete(self, *args, **kwargs):
		self.image.delete(save=False)
		super(Product, self).delete(*args, **kwargs)

	'''def getparams(self):
		params = {'производитель':{},
		          'коллекция':{},
		          'поверхность':{},
		          'тип':{}}
		proizvoditel = {}
		collection = {}
		surface = {}
		tip = {}
		proizvoditel['proizvoditel'] = [str(self.proizvoditel.id), str(self.proizvoditel.slug), str(self.proizvoditel)]
		collection['collection'] = [str(self.collection.id), str(self.collection.slug),str(self.collection)]
		surface['surface'] = [str(self.surface.id), str(self.surface.slug), str(self.surface)]
		tip['tip'] = [str(self.tip.id), str(self.tip.slug),str(self.tip)]
		params['производитель'] = proizvoditel
		params['коллекция'] = collection
		params['поверхность'] = surface
		params['тип'] = tip
		return params;'''
