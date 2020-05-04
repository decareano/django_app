from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view
from products.views import product_detail_view, product_create_view, render_initial_data, dynamic_lookup_view, product_delete_view, product_list_view
from covidapp.views import hospital_create_view, hospital_detail_view, hospital_list_view, hospital_index_view
from covidapp import views

app_name = 'covidapp'

urlpatterns = [
	path('createCovid', hospital_create_view),
	path('', views.hospital_index_view, name='hospital-index'),
	path('hospitals/', views.hospital_list_view, name='hospital-list'),
	path('<int:id>/', views.hospital_detail_view, name='hospital-detail'),
	#path('chart', hospital_chart_view)
	#path('<int:id>/', hospital_detail_view),
	path('product', product_detail_view, name='product-detail'),
    # path('create', product_create_view),
    # path('', product_list_view, name='product-list'),
    
    # path('initial', render_initial_data),
    # #path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    # path('<int:id>/delete/', product_delete_view, name='product-delete'),
   
]