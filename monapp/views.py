from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .forms import ProduitForm
from .models import Produit
from django.contrib import messages


def accueil(request):
    
    return render(request, 'monapp/accueil.html')

def liste_produits(request):
    produits = Produit.objects.all()  # Récupère tous les produits
    return render(request, 'monapp/produits.html', {'produits': produits})

def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit ajouté avec succès !")
            return redirect('liste_produits')  # redirige vers la liste après ajout
    else:
        form = ProduitForm()
    
    return render(request, 'monapp/ajouter_produit.html', {'form': form})