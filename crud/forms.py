from django import forms

class MonedasForm(forms.Form):

    # nombre = forms.CharField(label = "abreviacion", max_length = 30)
    
    nombre = forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control',
                                        'placeholder': 'Nombre de la Moneda'
        }),
        label = 'Nombre',
        max_length = 30
    )
    # abreviacion = forms.CharField(label = "abreviacion", max_length = 3)

    abreviacion= forms.CharField(
        widget = forms.TextInput(attrs={'class': 'form-control',
                                        'placeholder': 'Abreviacion'
        }),
        label = 'Abreviación',
        max_length = 3
    )
