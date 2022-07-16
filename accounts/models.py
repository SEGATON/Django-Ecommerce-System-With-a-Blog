from django.db import models

# Create your models here.


from django.contrib.auth.models import User

from PIL import Image




class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_image = models.ImageField(default='media/default.jpg', upload_to='media/users/profile_images', max_length=1000)

	def __str__(self):
		return f'{self.user.username}'


	def save(self,*args,**kwargs):

		super().save()

		img = Image.open(self.profile_image.path)

		if img.height > 500 or img.width > 600:
			output_size = (500,600)
			img.thumbnail(output_size)
			img.save(self.profile_image.path)




