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
