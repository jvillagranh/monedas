from django.db import models

# Create your models here.
class Monedas(models.Model):
    '''
    Modelos de Datos para almacenar las Monedas
    '''
    nombre      = models.CharField(max_length= 30, blank= False, unique= False)     # Nombre de la Moneda
    abreviacion = models.CharField(max_length= 3, blank= False, unique= True)       # Abreviacion de la Moneda

    def __str__(self):
        return self.nombre


class Paridades(models.Model):
    '''
    Modelo de Datos para almacenar las Paridades de las Monedas
    '''
    moneda  = models.ForeignKey(Monedas)                                            # Codigo Monedas
    fecha   = models.DateField()                                                    # Fecha Paridad Moneda
    paridad = models.DecimalField(max_digits= 10, decimal_places= 4)                # Valor Paridad Moneda

    def __str__(self):
        return str(self.moneda) + '-' + str(self.paridad)
