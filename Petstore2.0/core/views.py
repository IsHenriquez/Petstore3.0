
from django.shortcuts import render, redirect
from core.Carrito import Carrito

from core.models import Producto
# Create your views here.

def index(request):
    return render(request,'index.html')

def bandanas(request):
    return render(request,'bandanas.html')

def contacto(request):
    return render(request,'contacto.html')

def correas(request):
    return render(request,'correas.html')

def donaciones(request):
    return render(request,'donaciones.html')

def footer(request):
    return render(request,'footer.html')

def identificaciones(request):
    return render(request,'identificaciones.html')

def nav(request):
    return render(request,'nav.html')


def nosotros(request):
    return render(request,'nosotros.html')

def seguimiento(request):
    return render(request,'seguimiento.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

def inicio(request):
    return render(request,'inicio.html')

def login(request):
    return render(request,'login.html')

def historial(request):
    return render(request,'historial.html')

def carrito(request):
    return render(request,'carrito.html')





