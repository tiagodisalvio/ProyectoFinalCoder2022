from django.urls import path
from . import views

urlpatterns = [
    # path('usuario/crear', views.crear_usuario, name="crear_usuario"),
    path('post/crear', views.crear_post, name="crear_post"),
    path('pages/', views.lista_post, name="lista_post"),
    path('recomendaciones/', views.crear_recomendaciones, name="crear_recomendaciones"),
    path('pages/', views.DetallePost.as_view(), name="detalle_post"),
    path('pages/<int:pk>/editar', views.EditarPost.as_view(), name="editar_post"),
    path('pages/<int:pk>/borrar', views.BorrarPost.as_view(), name="borrar_post"),
]
