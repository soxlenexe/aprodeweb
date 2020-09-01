from django.db import models
from djrichtextfield.models import RichTextField

class Categoria(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.title


class Proyecto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name="proyectos", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    foto = models.URLField()

    intro = RichTextField()
    body = RichTextField()

    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Proyectos'


    def __str__(self):
        return self.title



class Slider(models.Model):
    title = models.CharField(max_length=90)
    body = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return self.title


class Pagina(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    foto = models.URLField()
    body = RichTextField()
    
    class Meta:
        verbose_name_plural = 'Paginas'

    def __str__(self):
        return self.title


class Seccion(models.Model):
    titulo = models.CharField(max_length=255)
    foto = models.URLField()
    body = RichTextField()

    class Meta:
        verbose_name_plural = 'Secciones'

    def __str__(self):
        return self.titulo


    

