from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pessoas/', views.pessoa, name="lend_pessoas")
]
