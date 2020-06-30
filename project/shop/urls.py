from django.urls import path
from . import views


urlpatterns = [
               path('dev/', views.index, name='home'),
               path('', views.main, name='main'),
               path('about/', views.about, name='about'),
               path('services/', views.services, name='services'),
               path('contacts/', views.contacts, name='contacts'),
               path('notebooks/', views.notebooks, name='notebooks'),
               path('smartphones/', views.smartphones, name='smartphones'),
               path('tablets/', views.tablets, name='tablets'),
               path('cart/', views.cart, name='cart'),
               path('product/<int:pk>/', views.product, name='product'),
               path('login/', views.login_page, name='login'),
               path('register/', views.register_page, name='register'),
               path('category/', views.category, name='category'),
               ]
