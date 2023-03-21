from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^dashboard_dim/', views.dashboard_dim, name='dashboard_dim'),
    url(r'^device_data_refresh/', views.device_data_refresh, name='device_data_refresh'),
    url(r'^device_dim_refresh/', views.device_dim_refresh, name='device_dim_refresh'),
    path('devices/', views.devices),
    path('about/', views.about),
    url('register/', views.registerPage),
    url('login/', views.loginPage, name="login"),
]

