from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Modelo_libros(models.Model):  
    id=models.AutoField(primary_key=True)  
    nombre_libro=models.CharField(max_length=50,verbose_name='Nombre de Libro',null=True)
    imagen_libro=models.ImageField(upload_to='imagenes/',verbose_name='Imagen',null=True)
    descripcion=models.CharField(max_length=100,verbose_name='Descripcion del Libro',null=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True)

    class Meta:
            db_table = 'tb_libros'


       