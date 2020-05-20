from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='html-home'),
    path('about/', views.about, name='html-about'),
]
