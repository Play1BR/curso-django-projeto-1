from django.http import HttpResponse
from django.urls import path

from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre)
]
