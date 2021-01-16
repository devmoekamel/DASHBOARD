from django.urls import path
from . import views
urlpatterns = [
path('',views.home, name='home'),
path('customer/<str:pk>/',views.customer,name='customer'),
path('product/',views.product,name='product'),
path('userpage/',views.userpage,name='user'),
path('create_order/<str:pk>/',views.create_order,name='create_order'),
path('create_customer/',views.create_customer,name='create_customer'),
path('update_order/<str:pk>/',views.update_order,name='update_order'),
path('delete_order/<str:pk>/',views.delete_order,name='delete_order'),
path('myaccount/',views.myaccount,name='myaccount'),

path('register/',views.register,name='register'),
path('login/',views.loginpage,name='login'),
path('logout/',views.logoutpage,name='logout'),



]
