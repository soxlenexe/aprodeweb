from django.shortcuts import render
from .models import Producto



def tienda(request):   
    productos = Producto.objects.all()

    context = {
        'productos': productos,
    }
    return render(request, 'tienda/tienda.html', context)