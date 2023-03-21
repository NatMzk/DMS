from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import device_power_consumption, device_dim
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm


# Create your views here.

def home(request):
	results = device_power_consumption.objects.order_by("id")[:10]
	devices = device_dim.objects.all()
	return render(request, 'accounts/dashboard.html', {'data': results, 'devices': devices})

def dashboard_dim(request):
	devices = device_dim.objects.all()
	return render(request, 'accounts/dashboard_dim.html', {'devices': devices})

def device_data_refresh(request):
    results = device_power_consumption.objects.order_by("id")[:10]
    return render(request, 'accounts/device_data_refresh.html', {'data': results})

def device_dim_refresh(request):
    devices = device_dim.objects.all()
    return render(request, 'accounts/device_dim_refresh.html', {'devices': devices})
	
def about(request):
	return render(request, 'accounts/about.html')

def devices(request):
	return render(request, 'accounts/devices.html')

def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form': form}
	return render(request, 'accounts/register.html', context)

def loginPage(request):
	return render(request, 'accounts/login.html')






