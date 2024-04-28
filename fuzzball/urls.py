from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.Formpage, name='Formpage'),
    path('submitpage/', views.submitpage, name='submitpage'),
    path('clear/', views.clear_submissions, name='clear_submissions'),
]