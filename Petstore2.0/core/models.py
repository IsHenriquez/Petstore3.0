from django.db import models
from django.forms import EmailField

# Create your models here.

class Usuario (models.Model):
        id_usuario = models.IntegerField(primary_key = True)
        nombre = models.CharField(max_length=15)
        apellidoPaterno = models.CharField(max_length=10)
        apellidoMaterno = models.CharField(max_length=10)
        email = EmailField()
        contraseña = models.CharField(max_length=10)
        telefono = models.IntegerField()
        direccion = models.IntegerField()
        comuna = models.CharField(max_length=15)
        region = models.CharField(max_length=15)

class TipoUser (models.Model):
        id_tipoUser =  models.IntegerField(primary_key = True)
        tipoUser = models.IntegerField()
        id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Categoria (models.Model):
        id_categoria = models.IntegerField(primary_key = True)
        descripcion = models.CharField(max_length=30)


class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()


class Descuento (models.Model):
        id_desucento = models.IntegerField(primary_key = True)
        promocion = models.BooleanField 
        subscripcion = models.BooleanField

class Venta (models.Model):
        id_venta = models.IntegerField(primary_key = True)
        fecha = models.DateField
        descripcion = models.CharField(max_length=200)
        total_vent = models.IntegerField()
        id_descuento = models.ForeignKey(Descuento, on_delete=models.PROTECT)
        id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
        id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
        id_categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

class Carrito (models.Model):
    id_carrito = models.IntegerField(primary_key = True)
    id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)


class Despacho (models.Model):
        id_despacho = models.IntegerField(primary_key = True)
        fecha = models.DateField
        descripcion = models.CharField(max_length=200)
        direccion = models.CharField(max_length=50)
        id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
        id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)


class Estado_despacho (models.Model):
        id_estado_despacho = models.IntegerField(primary_key = True)
        descripcion = models.CharField(max_length=30)
        id_despacho = models.ForeignKey(Despacho, on_delete=models.PROTECT)
        


class Historial(models.Model):
        id_historial = models.IntegerField(primary_key = True)
        id_despacho = models.ForeignKey(Despacho, on_delete=models.PROTECT)
        id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)


