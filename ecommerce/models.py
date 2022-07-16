from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField


from django.urls import reverse






def user_directory_path(instance, filename):
	return 'products/%Y/%m/%d/' .format(instance.id, filename)




#_______________________________________________________________________________________________________________/
class Brand(models.Model):

	name = models.CharField(max_length=300, null=True, blank=True)
	slug = models.SlugField(max_length=300, null=True)
	brand_logo = models.ImageField(upload_to='media/products/brands/logos', null=True, blank=True)

	def get_absolute_url(self):
		return reverse('products_catalog:single_brand', args=[self.slug])

	def __str__(self):
		return self.name





#_______________________________________________________________________________________________________________/
class Category(models.Model):

	name = models.CharField(max_length=100, null=True)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name



#_______________________________________________________________________________________________________________/
class Product(models.Model):


	class NewManager(models.Manager):
		def get_queryset(self):
			return super().get_queryset().filter(status='published')

	title = models.CharField(max_length=255, null=True)
	slug = models.SlugField(max_length=255, null=True)

	options = (('draft','Draft'),('published','Published'),)

	featured_image = models.ImageField(upload_to='media/product_imgs', null=True)

	product_image_1 = models.ImageField(upload_to='media/product_imgs', null=True, blank=True, max_length=3000)
	product_image_2 = models.ImageField(upload_to='media/product_imgs', null=True, blank=True, max_length=3000)
	product_image_3 = models.ImageField(upload_to='media/product_imgs', null=True, blank=True, max_length=3000)
	product_image_4 = models.ImageField(upload_to='media/product_imgs', null=True, blank=True, max_length=3000)
	product_image_5 = models.ImageField(upload_to='media/product_imgs', null=True, blank=True, max_length=3000)
	product_image_6 = models.ImageField(upload_to='media/product_imgs', null=True, blank=True, max_length=3000)
	product_image_7 = models.ImageField(upload_to='media/product_imgs', null=True, blank=True, max_length=3000)

	sku = models.CharField('SKU', max_length=100, null=True, blank=True)
	upc = models.CharField('UPC', max_length=100, null=True, blank=True)

	category = models.ForeignKey(Category, on_delete=models.PROTECT,default=1)

	brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True, blank=True)

	short_description = RichTextField(max_length=30000, null=True, blank=True)
	fulll_description = RichTextField(max_length=300000, null=True, blank=True)

	bullet_description_list = RichTextField(max_length=30000, null=True, blank=True)
	bullet_specifications_list = RichTextField(max_length=30000, null=True, blank=True)




	#publisher = models.ForeignKey(Profile, on_delete=models.PROTECT, null=True)


	price_regular = models.DecimalField('Regular price ',max_digits=6, decimal_places=2, null=True, blank=True)
	price_sale = models.DecimalField('Sale price', max_digits=6, decimal_places=2, null=True, blank=True)

	amz_price_regular = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
	amz_price_sale = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

	wal_price_regular = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
	wal_price_sale = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

	status = models.CharField(max_length=10, choices=options, default='draft', null=True)



	amazon = models.CharField(help_text='Amazon', max_length=400, null=True, blank=True)
	walmart = models.CharField('Walmart', max_length=400, null=True, blank=True)
	ebay = models.CharField('Ebay', max_length=400, null=True, blank=True)
	newegg = models.CharField('Newegg', max_length=400, null=True, blank=True)

	etsy = models.CharField('Etsy', max_length=400, null=True, blank=True)



	class Meta:
		verbose_name_plural = 'Products'



	def get_absolute_url(self):
		return reverse('ecommerce:single_product', args=[self.slug])


	def __str__(self):
		return self.title




#_______________________________________________________________________________________________________________/


























































