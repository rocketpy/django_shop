from django.urls import path
from . import views


urlpatterns = [
               path('', views.index, name='home'),
               path('about/', views.about, name='about'),
               path('services/', views.services, name='services'),
               path('contacts/', views.contacts, name='contacts'),
               path('item/<int:pk>/', views.items, name='items'),
               path('notebooks/', views.notebooks, name='notebooks'),
               path('smartphones/', views.smartphones, name='smartphones'),
               path('tablets/', views.tablets, name='tablets'),
               path('cart/', views.cart, name='cart'),
               path(r'^product/(?P<product_id>\w+)/$', views.product, name='product')
               ]
