from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver



class Categoria(models.Model):
    """ Categorias para clasificar las fotos """

    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()


    def __str__(self):
        return self.nombre


class Foto(models.Model):
    """ Fotos del album """

    categoria = models.ForeignKey(Categoria, null=True, blank=True,on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=50, default='No title')
    Foto = models.ImageField(upload_to='photos/')
    Fecha_publicacion = models.DateField(auto_now_add=True)
    Favorita = models.BooleanField(default=False)
    Comentario = models.CharField(max_length=200, blank=True)
    ##nombre = models.ManyToManyField(Categoria,null=True,blank=True)

    def __str__(self):
        return self.Titulo


@receiver(post_delete, sender=Foto)
def photo_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.foto.delete(False)
