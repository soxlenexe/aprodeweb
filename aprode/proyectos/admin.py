from django.contrib import admin

from  .models import Categoria, Proyecto, Pagina, Slider, Seccion

admin.site.register(Categoria)
admin.site.register(Proyecto)
admin.site.register(Pagina)
admin.site.register(Seccion)
#admin.site.register(Slider)