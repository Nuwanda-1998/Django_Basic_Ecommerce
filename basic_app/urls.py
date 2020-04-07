from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^registring/', views.registration, name='register_page'),
    url(r'^login_page/', views.Login_View, name='login'),
    url(r'^logout_page/', views.LogOut_View, name='logout'),
    url(r'^login_failed/', views.Invalid_p.as_view(), name='Invalid'),
    url(r'^product_adding/', views.Product_Adder_View, name='product_add'),
    url(r'6success_product_adding', views.Succes_Product_page.as_view(), name='Product_added'),
]
