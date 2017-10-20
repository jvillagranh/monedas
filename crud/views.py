from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Monedas
from crud.forms import MonedasForm


# Create your views here.
def index(request):

    #context = {}
    #return render(request, 'crud/index.html', context)

    monedas = Monedas.objects.all().order_by('id') # Traigame todas las monedas (select * from Monedas)
    #monedas = Monedas.objects.all().order_by('-id') # Ordena en forma descendente
    context = {'monedas': monedas, 'titulo': 'monedas'}
    return render(request, 'crud/index.html', context)

# Modificacion Clase
#def editar(request):
#    moneda =  get_object_or_404(Monedas,pk=1) # Traigame la moneda con id=1
#    context = {'moneda': moneda}
#    return render(request, 'crud/editar.html', context)


def editar(request, pk):
    moneda =  get_object_or_404(Monedas,pk=pk) # Traigame la moneda con id=1
    #print (request) #20/10/2017
    #print (request.GET) #20/10/2017

    # if request.method == 'GET':
    #     print("Estoy consultando")
    #
    #     # Arma Diccionar clave y valor.
    #     m = {'nombre': moneda.nombre,
    #         'abreviacion': moneda.abreviacion
    #         }
    #
    #     form = MonedasForm(m)

    if request.method == 'POST':
        print("En POST")

        form = MonedasForm(request.POST)

        if form.is_valid():
            print ("Formulario Valido")

            moneda.nombre = form.cleaned_data['nombre']
            moneda.abreviacion = form.cleaned_data['abreviacion']
            moneda.save()

            print ("Moneda Grabada !!!")

            #return redirect('/crud/')
            return redirect(reverse('crudindex'))

    else:
        print("Estoy Consultando")
        m = {'nombre': moneda.nombre,
            'abreviacion': moneda.abreviacion
        }
        form = MonedasForm(m)

    #20/10/2017 context = {'moneda': moneda, 'formulario': MonedasForm}
    context = {'moneda': moneda, 'formulario': form} #20/10/2017
    return render(request, 'crud/editar.html', context)



def nuevo(request):

    if request.method == 'POST':
        print("En POST")

        form = MonedasForm(request.POST)

        if form.is_valid():
            print ("Formulario Valido")

            moneda = Monedas()
            moneda.nombre = form.cleaned_data['nombre']
            moneda.abreviacion = form.cleaned_data['abreviacion']
            moneda.save()

            print ("Moneda creada" + str(moneda.id))

            return redirect(reverse('crudindex'))

    else:
        print ("Creando nueva moneda")
        form = MonedasForm()

    context = {'formulario': form}
    return render(request, 'crud/nuevo.html', context)


def eliminar(request, pk):

    moneda =  get_object_or_404(Monedas,pk=pk)

    if request.method == 'POST':
        print("En POST")
        moneda.delete()
        print("Moneda Borrada")
        return redirect(reverse('crudindex'))

    else:
        print("Estoy Consultando")
        m = {'nombre': moneda.nombre,
            'abreviacion': moneda.abreviacion
        }
        form = MonedasForm(m)

    context = {'moneda': moneda, 'formulario': form}
    return render(request, 'crud/eliminar.html', context)
