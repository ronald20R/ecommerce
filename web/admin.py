from django.contrib import admin

# Register your models here.
from .models import categoria, producto


admin.site.register(categoria)
#admin.site.register(producto)

#otro metodo con decoradores en python nos permite agregar funcionalidades especiales
@admin.register(producto)

class productoAdmin(admin.ModelAdmin):
    #con tuplas podemos agregar campos a la vista
    list_display = ('nombre', 'categoria', 'precio', 'fecha_registro')
    list_editable = ('precio',)

    search_fields = ('nombre','categoria__nombre')