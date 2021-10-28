"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import apiview as myapi
urlpatterns = [
    path('base', views.base,name='base'),
    path('test', views.test,name='test'),
    path('signup', views.signup,name='signup'),
    path('', views.index,name='index'),
    path('track_list', views.track_list,name='track_list'),


    path('userpanel', views.userpanel,name='userpanel'),
    path('userview', views.userview,name='userview'),
    path('view_product', views.view_products,name='view_product'),
    path('view_product_admin', views.view_products_admin,name='view_product_admin'),
    path('view_product_backery', views.view_products_backery,name='view_product_backery'),
    path('view_product_fruits', views.view_products_fruits,name='view_product_fruits'),
    path('view_product_vegitable', views.view_products_vegitable,name='view_product_vegitable'),
    path('view_product_own', views.view_products_own,name='view_product_own'),
    path('cart_items', views.cart_items,name='cart_items'),
    path('view_cart', views.view_cart,name='view_cart'),
    path('view_track_order/<int:id>', views.track_order,name='view_track_order'),
    path('view_tracking_list', views.track_list,name='view_tracking_list'),
    path('manage_address', views.manage_address,name='manage_address'),
    path('view_userdata', views.userdatas,name='view_userdata'),
    path('orderdetails', views.orderdetails,name='orderdetails'),
    path('orderdetailsview/<int:id>/', views.orderdetailsview,name='orderdetailsview'),
    path('markasdelivered/<int:id>/', views.markasdelivered,name='markasdelivered'),
    path('markasdelivereduser/<int:id>/', views.markasdelivereduser,name='markasdelivereduser'),
    path('FeedbackView/<int:id>/', views.FeedbackView,name='FeedbackView'),
    path('ViewFeedBack/<int:id>/', views.ViewFeedBack,name='ViewFeedBack'),
    path('ViewFeedBackAdmin/<int:id>/', views.ViewFeedBackAdmin,name='ViewFeedBackAdmin'),



    path('create_product', views.create_product,name='create_product'),
    path('add_to_cart/<int:id>/', views.add_to_cart,name='add_to_cart'),
    path('add_quantity/<int:id>/', views.add_quantity,name='add_quantity'),
    path('remove_quantity/<int:id>/', views.remove_quantity,name='remove_quantity'),
    path('payform/', views.payform,name='paymentform'),
    path('payed/', views.payed,name='payed'),
    path('delivery_address/', views.Delivery_address,name='delivery_address'),


    path('delete_product/<int:id>/',views.delete_product,name='delete_product'),
    path('delete_cart/<int:id>/',views.delete_cart,name='delete_cart'),
    path('delete_delivery_address/<int:id>/',views.delete_delivery_address,name='delete_delivery_address'),


    path('update_product/<int:id>/',views.update_products,name='update_product'),
    path('update_delivery_address/<int:id>/',views.update_delivery_address,name='update_delivery_address'),


    path('primary_address/<int:id>/',views.set_primary_address,name='set_primary'),

    ########## activate or deactivate ########

    path('activate/<int:id>/', views.activate, name='activate'),
    path('deactivate/<int:id>/', views.deactivate, name='deactivate'),

    ### searchfield ###
    path('searchfield', views.searchfield, name='searchfield'),





    ##################### api ###################

    path('apiview',myapi.some_view,name='some_view'),
    path('userlogin',myapi.userlogin,name='userlogin'),
    path('UserRegister',myapi.UserRegister,name='UserRegister'),
    # path('delete/<int:id>/',myapi.delete,name='delete'),


]



