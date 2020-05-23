from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from .models import UserProfileDB, UserPersonalityDB, QuestionsDB
from .serializers import UserProfileDBSerializer, UserPersonalityDBSerializer, QuestionsDBSerializer

def home(request):
    return render(request, 'html/home.html')


def about(request):
    return render(request, 'html/about.html', {'title': 'About'})

@csrf_exempt
def get_users_profiles(request):
    """
        List all user profiles, or create a new user profile.
    """
    if request.method == 'GET':
        userProfiles = UserProfileDB.objects.all()
        serializer = UserProfileDBSerializer(userProfiles, many=True)
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse(status=404)

@csrf_exempt
def add_user_profile(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserProfileDBSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    return HttpResponse(status=404)


@csrf_exempt
def get_one_user_profile(request, pk):
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




@csrf_exempt
def all_cnps(request):
    """
        List all user profiles, or create a new user profile.
    """
    if request.method == 'GET':
        userCNP = UserPersonalityDB.objects.all()
        serializer = UserPersonalityDBSerializer(userCNP, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def get_user_cnp(request, pk):
    """
        List all user profiles, or create a new user profile.
    """
    try:
        userCNP = UserPersonalityDB.objects.filter(userid=pk)
        print(userCNP)
    except UserPersonalityDB.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserPersonalityDBSerializer(userCNP, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def add_new_user_cnp(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserPersonalityDBSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def questions__and_answers(request):
    """
        List all user profiles, or create a new user profile.
    """
    if request.method == 'GET':
        questions = QuestionsDB.objects.all()
        serializer = QuestionsDBSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse(status=404)


@csrf_exempt
def one_questions_and_answers(request, pk):
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
    return HttpResponse(status=404)
