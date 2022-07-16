from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
# Create your models here.

from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey



from ckeditor.fields import RichTextField










class Category(MPTTModel):

	name = models.CharField(max_length=100, null=True,default=None)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

	class MPTTMeta:
		order_insertion_by = ['name']
		verbose_name_plural = 'Categories'

	def get_absolute_url(self):
		return reverse('blog:category_details_view', args=[str(self.slug)])

	def __str__(self):
		return self.name





def user_directory_path(instance, filename):
	return 'posts/%Y/%m/%d/' .format(instance.id, filename)




class Post(models.Model):


	class NewManager(models.Manager):
		def get_queryset(self):
			return super().get_queryset().filter(status='published')


	options = (('draft','Draft'),('published','Published'),)
	title = models.CharField(max_length=300,null=True)
	category = TreeForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True, default=None)
	excerpt = RichTextField(blank=True,max_length=30000,null=True)
	slug = models.SlugField(max_length=300, unique_for_date='published',null=True)
	featured_image = models.ImageField(upload_to='media/blog_featured_images', null=True)
	published = models.DateTimeField(default=timezone.now)
	author  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts',null=True)
	content  = RichTextField(blank=True,null=True)
	status =  models.CharField(max_length=10, choices=options, default='draft',null=True)

	objects = models.Manager()
	newmanager = NewManager()



	def get_absolute_url(self):
		return reverse('blog:single_post', args=[self.slug])

	class Meta:
		ordering = ('-published',)
		verbose_name_plural = 'Posts'
		unique_together = ('title','slug')

	def __str__(self):
		return self.title







