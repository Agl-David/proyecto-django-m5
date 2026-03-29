from django.contrib import admin

from .models import Categoria
from .models import Producto

"""
Categoria
"""
admin.site.register(Categoria)

"""
Producto
"""
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "unidades", "disponible",)
    ordering = ["precio"]
    search_fields = ["nombre"]
    list_filter = ("disponible",)

admin.site.register(Producto, ProductoAdmin)

# Register your models here.
