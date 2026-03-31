from django.urls import path, include 
from . import views 

urlpatterns = [
  path('contact/<str:name>', views.contact),
  path('categorias', views.categorias, name="categorias"),
  path(
       'demo', views.index
  )
]