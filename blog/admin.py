from django.contrib import admin

from .models import Post,Category
# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from . import models


class CategoryAdmin(DraggableMPTTAdmin):
	pass


admin.site.register(Post)
admin.site.register(models.Category,CategoryAdmin)