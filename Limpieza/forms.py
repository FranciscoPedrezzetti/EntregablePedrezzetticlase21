from django import forms


class quimForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    proveedor=forms.CharField(max_length=50)
    prodxbulto=forms.IntegerField() 

class cepiForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    proveedor=forms.CharField(max_length=50)
    prodxbulto=forms.IntegerField() 

class descaForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    proveedor=forms.CharField(max_length=50)
    prodxbulto=forms.IntegerField() 