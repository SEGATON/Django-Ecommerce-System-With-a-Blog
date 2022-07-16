from django.shortcuts import render

# Create your views here.








def index(request): 
	return render(request, 'django_experiments_app/index.html', {

		})



def front_page(request): 
	return render(request, 'django_experiments_app/front_page.html', {

		})