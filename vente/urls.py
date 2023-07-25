from django.urls import path
from .views import accueilVenteView
from .views import aboutView
from .views import contactView

urlpatterns = [
    path('', accueilVenteView, name="index"),
    path('about/', aboutView, name="about"),
    path('contact/', contactView, name="contact")

]
