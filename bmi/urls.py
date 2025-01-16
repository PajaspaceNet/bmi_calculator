from django.urls import path
from . import views

urlpatterns = [
 # tohle funguje - sice blbe
 # path('', views.bmi_calculator, name='bmi_calculator'),  # Výchozí stránka
 #tohle ne
 #path('', views.index, name='index'),  # Výchozí stránka

#tady musi by jmeno funkce u view !!!
path("", views.bmi_calculator, name="bmi_calculator"),

]

