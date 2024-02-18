from django.urls import path
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home),
    path('contacts/', views.contacts),
    path('product/', views.product)
]