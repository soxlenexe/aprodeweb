from django.shortcuts import render
from .models import Categoria, Proyecto, Slider, Pagina, Seccion

def frontpage(request):
    secciones = Seccion.objects.all()
    context = {
        'secciones': secciones,
    }

    return render(request, 'frontend.html', context)



def proyectos(request):
    
    proyectos = Proyecto.objects.all()

    context = {
        'proyectos': proyectos,
    }

    return render(request, 'proyectos/listado.html', context)


def proyecto(request, slug):
    
    proyecto = Proyecto.objects.get(slug=slug)

    context = {
        'proyecto': proyecto,
    }

    return render(request, 'proyectos/proyecto.html', context)


def ong(request, slug):
    
    page = Pagina.objects.get(slug=slug)

    context = {
        'page': page,
    }

    return render(request, 'page/page.html', context)
