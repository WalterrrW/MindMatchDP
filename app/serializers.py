from rest_framework import serializers
from .models import UserProfileDB, UserPersonalityDB, QuestionsDB

class UserProfileDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileDB
        fields = [
            'userid',
            'description',
            'random_fun'
        ]