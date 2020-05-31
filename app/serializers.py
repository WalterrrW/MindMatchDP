from rest_framework import serializers
from .models import UserProfileDB, UserPersonalityDB, QuestionsDB
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'id'
        ]

class UserProfileDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileDB
        fields = [
            'userid',
            'description',
            'random_fun'
        ]


class UserPersonalityDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPersonalityDB
        fields = [
            'userid',
            'cnp'
        ]


class QuestionsDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsDB
        fields = [
            'question',
            'asnwer_a',
            'asnwer_b',
            'asnwer_c'
        ]
