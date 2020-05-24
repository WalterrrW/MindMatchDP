from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import UserProfileDB, UserPersonalityDB, QuestionsDB

class UserSerializer(serializers.HyperlinkedModelSerializer):
    #userProfile = serializers.HyperlinkedRelatedField(read_only=True, view_name = 'UserProfileDB-detail')

    class Meta:
        model = User
        fields = [
            'url',
            'username',
            'email',
            'groups'
        ]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [
            'url',
            'name'
        ]

class UserProfileDBSerializer(serializers.HyperlinkedModelSerializer):
    #user = serializers.ReadOnlyField(source = 'user.username') #???
    class Meta:
        model = UserProfileDB
        fields = [
            'userid',
            'description',
            'random_fun'
        ]

class UserPersonalityDBSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserPersonalityDB
        fields = [
            'userid',
            'cnp'
        ]


class QuestionsDBSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionsDB
        fields = [
            'question',
            'asnwer_a',
            'asnwer_b',
            'asnwer_c'
        ]