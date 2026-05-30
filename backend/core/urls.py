from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('link/<slug:slug>/', short_link, name="short_link"),
    path('<slug:slug>/', get_link, name="get_link"),
]