from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('start_game/', views.index, name='start_game'),
    # Other URL patterns...
]
