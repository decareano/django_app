"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include,path
from pages.views import home_view, contact_view, about_view, my_page_view
from products.views import product_detail_view, product_create_view, render_initial_data, dynamic_lookup_view, product_delete_view, product_list_view
from covidapp.views import hospital_create_view, hospital_detail_view, hospital_list_view

urlpatterns = [
    path('createCovid', hospital_create_view),
    #path('covidapp/', include('covidapp.urls')),
    #path('oneCovid/', hospital_detail_view, name='product-delete'),
    path('oneCovid/<int:id>/', hospital_detail_view, name='product-detail'),
    path('covidapp/', hospital_list_view, name='hospital-list'),
    path('blog/', include('blog.urls')),
    path('products/', include('products.urls')),
    path('', home_view, name='home'),
    path('contact/', contact_view),
    #path('<int:id>/', product_detail_view, name='product-detail'),
    #path('product/', product_detail_view, name='product-detail'),
    path('create/', product_create_view, name='product-create'),
    path('products/', product_list_view, name='product-list'),
    path('admin/', admin.site.urls),
    path('about/', about_view),
    path('initial', render_initial_data),
    #path('products/<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('products/<int:id>/delete/', product_delete_view, name='product-delete'),
    path('pageview/', my_page_view, name='page-view')
]
