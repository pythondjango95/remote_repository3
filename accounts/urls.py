from django.urls import path
from accounts import views
urlpatterns = [
    path('', views.home,name='home'),
    path('product', views.products,name='product'),
    path('customer/<pk>', views.customer,name='customer'),
    path('order', views.orders,name='order'),
    path('update_order/<pk>', views.update_order,name='update_order'),
    path('delete_order/<pk>', views.delete_order,name='delete_order'),
    path('add_product', views.add_product,name='add_product'),
    path('update_product/<pk>', views.update_product,name='update_product'),
    path('delete_product/<pk>', views.delete_product,name='delete_product'),
    path('add_order', views.add_order,name='add_order'),

]

