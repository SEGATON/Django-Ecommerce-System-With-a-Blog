from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import RegisterForm,UserUpdateForm,ProfileUpdateForm

from django.urls import reverse







def register(request):
	

		if request.method == "POST":
			register_form = RegisterForm(request.POST)
			if register_form.is_valid():
				register_form.save()
				username = register_form.cleaned_data.get('username')
				messages.success(request, f' Account created for {username}!')
				return redirect('accounts:login')

		else:
			register_form = RegisterForm()

		return render(request,'registration/register.html', {'register_form':register_form})




@login_required 
def profile(request):

	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save() 

			messages.success(request, f'Your account has been updated.')

			return redirect('accounts:profile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}


	return render(request, 'registration/profile.html', context)

































