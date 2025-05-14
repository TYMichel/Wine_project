from django.urls import path 
from . import views


urlpatterns = [
     path('',views.acceuil_view,name="welcome-view"),
     path('acceuil/',views.acceuil_view,name="acceuil-view"),
     path('acceuil/<str:prenom>/',views.welcome_view,name="test1")
]