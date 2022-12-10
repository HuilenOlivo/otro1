from django import forms


class formTodo(forms.Form):
    nota=forms.CharField(max_length=200)
    pendiente=forms.BooleanField()
    
class formContact(forms.Form):
    nombre = forms.CharField(max_length=40)
    telefono = forms.IntegerField()
    correo = forms.EmailField()
   
class formProyecto(forms.Form):
    nombre = forms.CharField(max_length=40)
    descripcion = forms.CharField()