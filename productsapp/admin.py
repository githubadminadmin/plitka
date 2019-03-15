from django.contrib import admin
from .models import ProductCategory, Product, ProductTypeSurface, ProductProizvoditel, ProductColor, ProductСollection, ProductCountry, ProductType, CompositionsCollection

# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class ProductTypeSurfaceAdmin(admin.ModelAdmin):

	prepopulated_fields = {'slug': ('name',)}

class ProductProizvoditelAdmin(admin.ModelAdmin):
	fields = (('name', 'slug'), 'productcountry', 'image', 'description')
	list_display = ['name', 'productcountry']
	prepopulated_fields = {'slug': ('name',)}
	list_filter = ('productcountry',)

class ProductColorAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}


class CompositionsCollectionItemInline(admin.TabularInline):
	model = CompositionsCollection
	raw_id_field = ['name']

class ProductCollectionAdmin(admin.ModelAdmin):
	fields = (('name', 'slug'), 'productcategory', 'productproizvoditel', 'image', 'description', 'novinka', 'sale', 'available')
	list_display = ['name', 'productproizvoditel', 'available']
	prepopulated_fields = {'slug': ('name',)}
	list_filter = ('productproizvoditel', 'productcategory')
	list_editable = ['available']
	inlines = [CompositionsCollectionItemInline]

class ProductTypeAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}


class ProductCountryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ['name', 'category', 'image_img', 'image', 'stock', 'price','hits','available']
	exclude = ('area', 'hits')
	list_editable = ['price', 'available', 'stock', 'image', 'hits']


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductTypeSurface, ProductTypeSurfaceAdmin)
admin.site.register(ProductProizvoditel, ProductProizvoditelAdmin)
admin.site.register(ProductColor, ProductColorAdmin)
admin.site.register(ProductСollection, ProductCollectionAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(ProductCountry, ProductCountryAdmin)