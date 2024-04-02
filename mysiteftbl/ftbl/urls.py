from django.urls import path
from . import views
from .views import my_diagrams  # Import my_diagrams from views.py

urlpatterns = [
    path("", views.index, name="index"),
    path('realmadrid21-22/', views.my_diagrams, name='realmadrid21-22'),  # Use my_diagrams in urlpatterns
]
