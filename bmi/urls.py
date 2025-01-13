from django.urls import path
from . import views

urlpatterns = [
  path('', views.bmi_calculator, name='bmi_calculator'),  # Výchozí stránka

    #path('', views.index, name='index'),  # Výchozí stránka
]

