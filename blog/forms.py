from django import forms
from ckeditor.fields import RichTextFormField
from pkg_resources import require

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    usuario= forms.CharField(max_length=10)

class PostFormulario(forms.Form):
    titulo=forms.CharField(max_length=120)
    subtitulo=forms.CharField(max_length=100)
    contenido=RichTextFormField(required=False)
    imagen= forms.ImageField(required=False)
    autor= forms.CharField(max_length=50)
    # fecha=forms.DateTimeField(auto_now_add=True)
    # actualizado=forms.DateTimeField(auto_now=True)

class BusquedaPosts(forms.Form):
    titulo=forms.CharField(max_length=20)

class RecomendacionesFormulario(forms.Form):
    asunto=forms.CharField(max_length=120)
    contenido=RichTextFormField(required=False)
    # fecha=forms.DateTimeField(auto_now_add=True)
    # actualizado=forms.DateTimeField(auto_now=True)