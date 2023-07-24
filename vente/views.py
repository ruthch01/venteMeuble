from django.shortcuts import render
from .models import Article


# Create your views here.
# request permet d envoyer ou de recuperer les donnee via le http
# context permet d envoyer le code python vers le  html


def accueilVenteView(request, template_name="meuble/pages/index.html"):
    # declaration de notre context
    context = {}
    bonjour = "Bonjour tout le monde"
    # affectation de la clef dans notre context
    # recuperation de la clef
    #       clef     VALEUR

    # instance Article
    a1 = Article("Chaise", "Meuble de salon ")
    a2 = Article("Table", "Meuble de salon ")
    a3 = Article("Fauteuil", "Meuble de salon ")
    a4 = Article("Vitrine", "Meuble de salon ")
    a5 = Article("Tabouret", "Meuble de salon ")
    a6 = Article("Table_Télévisur", "Meuble de salon ")
    a7 = Article("Mini-Bar", "Meuble de salon ")
    a8 = Article("Armoir", "Meuble de salon ")
    list_article = [a1, a2, a3, a4, a5, a6, a7, a8]
    for art in list_article:
        print(art)
    print(a1.title)
    print(a1.description)
    context['name'] = bonjour
    context['article'] = list_article

    return render(request, template_name, context)


def aboutView(request, template_name="meuble/pages/about.html"):
    # declaration de notre context

    context = {}
    bonjour = "Bonjour tout le monde"

    # affectation de la clef dans notre context
    # recuperation de la clef
    #       clef     VALEUR
    context['name'] = bonjour
    return render(request, template_name, context)
