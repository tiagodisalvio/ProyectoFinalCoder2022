from django.shortcuts import render, redirect
from .models import Post, Recomendaciones
from .forms import PostFormulario, BusquedaPosts, RecomendacionesFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
# Create your views here.

@login_required
def crear_post(request):

    if request.method == 'POST':
        form = PostFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            post = Post(titulo=data['titulo'], subtitulo=data['subtitulo'] ,autor=data['autor'] ,contenido=data['contenido'])
            post.save()
            return redirect('index')
    
    form = PostFormulario()
    return render(request, "blog/crear_post.html", {'form': form})

def lista_post(request):
    
    titulo_a_buscar = request.GET.get('nombre', None)
    
    if titulo_a_buscar is not None:
        posts = Post.objects.filter(nombre__icontains=titulo_a_buscar)
    else:
        posts = Post.objects.all()
        
    form = BusquedaPosts()
    return render(request, "blog/lista_post.html", {'form': form, 'posts': posts})

class DetallePost(DetailView):
    model= Post
    template_name= "/blog/detalle_post.html"

class EditarPost(LoginRequiredMixin, UpdateView):

    model= Post
    success_url = '/blog/pages/'
    fields= ['titulo', 'subtitulo', 'contenido']

class BorrarPost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/pages/'
    

def crear_recomendaciones(request):

    if request.method == 'POST':
        form = RecomendacionesFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            recomendacion = Recomendaciones(asunto=data['asunto'], contenido=data['contenido'])
            recomendacion.save()
            return redirect('index')
    
    form = RecomendacionesFormulario()
    return render(request, "blog/crear_recomendaciones.html", {'form': form})