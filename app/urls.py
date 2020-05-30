from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-refresh/', refresh_jwt_token),

    path('profile/', views.get_users_profiles, name='get_users_profiles'),
    path('profile/new/', views.add_user_profile, name='add_user_profile'),
    path('profile/<int:pk>/', views.get_one_user_profile, name='get_one_user_profile'),

    path('cnp/', views.all_cnps, name='all_cnps'),
    path('cnp/new/', views.add_new_user_cnp, name='add_new_user_cnp'),
    path('cnp/<int:pk>/', views.get_user_cnp, name='get_user_cnp'),

    path('question/', views.questions__and_answers, name='question'),
    path('question/<int:pk>/', views.one_questions_and_answers, name='question'),

    path('match/<int:pk>/', views.matching, name='matching'),

    path('about/', views.about, name='html-about'),
]
