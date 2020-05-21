from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='html-home'),
    path('userprofiles/', views.userProfileList, name='userprofiles'),
    path('userprofiles/<int:pk>/', views.userProfileDetail, name='userprofile'),
    path('usercnp/', views.userCNP, name='userCNP'),
    path('question/', views.other_questions_answers, name='question'),
    path('question/<int:pk>/', views.questions_answers, name='question'),
    path('about/', views.about, name='html-about'),
]
