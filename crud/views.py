from django.shortcuts import render, get_object_or_404
from .models import Monedas


# Create your views here.
def index(request):

    #context = {}
    #return render(request, 'crud/index.html', context)

    monedas = Monedas.objects.all() # Traigame todas las monedas (select * from Monedas)
    context = {'monedas': monedas, 'titulo': 'monedas'}
    return render(request, 'crud/index.html', context)


#def editar(request):

#    moneda =  get_object_or_404(Monedas,pk=1) # Traigame la moneda con id=1
#    context = {'moneda': moneda}
#    return render(request, 'crud/editar.html', context)


def editar(request, pk):

    moneda =  get_object_or_404(Monedas,pk=pk) # Traigame la moneda con id=1
    context = {'moneda': moneda}
    return render(request, 'crud/editar.html', context)
