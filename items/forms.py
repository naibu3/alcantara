from django import forms

class CreateItemForm(forms.Form):

    PLACES = [('cocina', 'Cocina'), ('cuarto', 'Cuarto')]

    name = forms.CharField(label="Nombre del item",
                           max_length=50)
    comment = forms.CharField(label="Comentario",
                              widget=forms.Textarea,
                              required=False)
    uds =  forms.IntegerField(label="Numero de unidades")
    place = forms.ChoiceField(
        label='Select an option',
        choices=PLACES)
    
class UpdateItemForm(forms.Form):

    PLACES = [('cocina', 'Cocina'), ('cuarto', 'Cuarto')]

    name = forms.CharField(label="Nombre del item",
                           max_length=50)
    comment = forms.CharField(label="Comentario",
                              widget=forms.Textarea,
                              required=False)
    uds =  forms.IntegerField(label="Numero de unidades")
    place = forms.ChoiceField(
        label='Select an option',
        choices=PLACES)