from django.db import models


class Producto(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    foto = models.URLField()
    intro = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.title
    

