# monapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('produits/', views.liste_produits, name='liste_produits'), #<-- this for show products
    path('ajouter/', views.ajouter_produit, name='ajouter_produit'),#<-- this for add products
]
