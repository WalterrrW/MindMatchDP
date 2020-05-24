from .models import UserProfileDB, UserPersonalityDB, QuestionsDB
from .serializers import UserProfileDBSerializer, GroupSerializer, UserSerializer, UserPersonalityDBSerializer, QuestionsDBSerializer
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserProfileDBViewSet(viewsets.ModelViewSet):
    queryset = UserProfileDB.objects.all()
    serializer_class = UserProfileDBSerializer

class UserPersonalityDBViewSet(viewsets.ModelViewSet):
    queryset = UserPersonalityDB.objects.all()
    serializer_class = UserPersonalityDBSerializer

class QuestionsDBViewSet(viewsets.ModelViewSet):
    queryset = QuestionsDB.objects.all()
    serializer_class = QuestionsDBSerializer