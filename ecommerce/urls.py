from django.urls import path
from . import views  

app_name = 'ecommerce'

urlpatterns = [

	path('browse_products/', views.browse_products, name='browse_products'),
	path('<slug:product>/', views.single_product, name='single_product'),









]
