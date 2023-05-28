
from django.urls import path
from .views import *

urlpatterns = [
    path('alpha/', search, name='alpha'),
]