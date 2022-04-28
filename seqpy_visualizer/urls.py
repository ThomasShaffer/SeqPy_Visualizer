from django.urls import path
from . import views

urlpatterns = [
    path('create/<str:given_name>/<str:given_sequence>/', views.createDna, name='create-dna'),
    path('dna/<str:primary_key>/delete', views.deleteDna, name='delete-dna'),
    path('dna/<str:primary_key>/update/', views.updateDna, name='update-dna'),
    path('dna/<str:primary_key>/<str:computation>/', views.computeDna, name='compute-dna'),
    path('dna/<str:primary_key>/', views.getDna, name='dna'),
    path('dna/', views.getDnas, name='dna'),
    path('dna/create', views.createDna, name='create-dna'),
    path('index/', views.index, name='routes'),
    path('', views.getRoutes, name = 'home'),
]