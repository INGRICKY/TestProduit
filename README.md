# 🐍 Projet Django - Gestion de Produits

Ce projet est une application web développée avec **Django** permettant de gérer des produits (ajout, affichage, disponibilité).

## 🚀 Fonctionnalités

- Page d'accueil stylisée avec Bootstrap
- Ajout de produits via formulaire
- Liste des produits avec affichage en tableau
- Système de template réutilisable (`base.html`)
- Navigation simple avec barre de menu
- Messages de confirmation utilisateur

## 📦 Installation

```bash
git clone https://github.com/ton_utilisateur/mon-projet-django.git
cd mon-projet-django
python -m venv venv
source venv/bin/activate   # ou venv\Scripts\activate sur Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
