from django.urls import path
from .views import accueilVenteView
from .views import aboutView

urlpatterns = [
    path('', accueilVenteView, name="index"),
    path('about', aboutView, name="about")

]
