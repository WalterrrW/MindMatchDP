from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import UserProfileDB, UserPersonalityDB, QuestionsDB
from .serializers import UserProfileDBSerializer

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
