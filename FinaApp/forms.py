from django import forms


# Se definen formularios
class BajistasFORM(forms.Form):

    nombre =  forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    email = forms.EmailField()


class BateristasFORM(forms.Form):

    nombre =  forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    email = forms.EmailField()

class GuitarristasFORM(forms.Form):

    nombre =  forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    email = forms.EmailField()