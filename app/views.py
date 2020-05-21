from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from .models import UserProfileDB, UserPersonalityDB, QuestionsDB
from .serializers import UserProfileDBSerializer, UserPersonalityDBSerializer, QuestionsDBSerializer


@csrf_exempt
def userProfileList(request):
    """
        List all user profiles, or create a new user profile.
    """
    if request.method == 'GET':
        userProfiles = UserProfileDB.objects.all()
        serializer = UserProfileDBSerializer(userProfiles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserProfileDBSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def userProfileDetail(request, pk):
    """
    Retrieve, update or delete a user profile.
    """
    try:
        userProfile = UserProfileDB.objects.get(pk=pk)
    except UserProfileDB.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserProfileDBSerializer(userProfile)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserProfileDBSerializer(userProfile, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        userProfile.delete()
        return HttpResponse(status=204)


def home(request):
    return render(request, 'html/home.html')


def about(request):
    return render(request, 'html/about.html', {'title': 'About'})


@csrf_exempt
def userCNP(request):
    """
        List all user profiles, or create a new user profile.
    """
    if request.method == 'GET':
        userCNP = UserPersonalityDB.objects.all()
        serializer = UserPersonalityDBSerializer(userCNP, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserPersonalityDBSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def questions_answers(request, pk):
    """
    Retrieve, update or delete a user profile.
    """
    try:
        questions_answers = QuestionsDB.objects.get(pk=pk)
    except QuestionsDBSerializer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuestionsDBSerializer(questions_answers)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuestionsDBSerializer(questions_answers, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        QuestionsDBSerializer.delete()
        return HttpResponse(status=204)


@csrf_exempt
def other_questions_answers(request):
    """
        List all user profiles, or create a new user profile.
    """
    if request.method == 'GET':
        questions = QuestionsDB.objects.all()
        serializer = QuestionsDBSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionsDBSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)