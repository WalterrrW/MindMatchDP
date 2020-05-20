from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='html-home'),
    path('userprofiles/', views.userProfileList, name='userprofiles'),
    path('userprofiles/<int:pk>/', views.userProfileDetail, name='userprofile'),
    path('about/', views.about, name='html-about'),
]
