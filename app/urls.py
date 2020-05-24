from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'usersProfile', views.UserProfileDBViewSet)
router.register(r'userspersonality', views.UserPersonalityDBViewSet)
router.register(r'questions', views.QuestionsDBViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
