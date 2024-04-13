from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_products, name='index'),
    path('add-developer', views.add_developer),
    path('add-product', views.add_product)
]