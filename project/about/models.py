from django.db import models


class Description(models.Model):
    texto = models.TextField(verbose_name="Texto")
    image = models.ImageField(verbose_name="Imagen", upload_to= 'projects')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    
    class Meta:
        verbose_name = "decripcion"
        verbose_name_plural = "descripciones"