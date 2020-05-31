from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from .models import UserProfileDB, UserPersonalityDB, QuestionsDB
from .serializers import UserProfileDBSerializer, UserPersonalityDBSerializer, QuestionsDBSerializer, UserSerializer, UserSerializerOnlyId
from rest_framework import viewsets, permissions

import json
from django.core.serializers.json import DjangoJSONEncoder
import re

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

@csrf_exempt
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse(status=404)

@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(serializer.errors, status=400)
        #return HttpResponse(status=404)
    return HttpResponse(status=404)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if User.objects.filter(username=data['username']).filter(password=data['password']).exists():
            data['id']=re.findall(r'\d+',str(User.objects.filter(username=data['username']).filter(password=data['password']).values('id')))[0]
            return JsonResponse(data, status=201, safe=False)
        else:
            return HttpResponse(status=403)
    return HttpResponse(status=404)
    # if request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     # if User.objects.filter(username=data['username']).filter(password=data['password']).exists():
    #     #     # qs = User.objects.filter(username=data['username']).filter(password=data['password']).values('id')
    #     #     #serialized_qs = json.dumps(list(qs))
    #     #     #return JsonResponse(serialized_qs,safe=False)
    #     else:
    #         return HttpResponse(status=403)
    # return HttpResponse("GET requests only!")


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


@csrf_exempt
def matching(request, pk):
    if request.method == 'GET':
        matched_list = get_matching_users_profile(pk, UserPersonalityDB.objects.filter(userid=pk).first().cnp)
        matched_list = get_matching_profiles(matched_list)
        print(matched_list)
        serializer = UserProfileDBSerializer(matched_list, many=True)
        return JsonResponse(serializer.data, safe=False)
    return HttpResponse(status=404)


def get_matching_users_profile(pk, cnp):
    personality_list = UserPersonalityDB.objects.all()
    final_order = []
    for x in personality_list:
        # print(pk)
        # print(x.userid.id)
        if x.userid.id != pk:
            # ---------------implement algo
            # procent_matched = x.userid.id + 75
            procent_matched = get_procent_matched(cnp, x.cnp)
            # print(procent_matched)
            # ---------------- implement algo
            final_order.append((x.userid.id, procent_matched))
    final_order = sorted(final_order, key=lambda x: -x[1])
    print(final_order)
    return final_order


def get_matching_profiles(matched_list):
    matched_profiles = []
    user_profiles = UserProfileDB.objects.all()

    for x in matched_list:
        profile = user_profiles.filter(userid=x[0]).first()
        print(profile)
        matched_profiles.append(profile)
    return matched_profiles


def get_procent_matched(own_cnp, foreign_cnp):
    own_cnp_list = list(own_cnp)
    foreign_cnp_list = list(foreign_cnp)
    # print(own_cnp_list)
    # print(foreign_cnp_list)
    score = 0

    for x in range(0, len(own_cnp_list)):
        if (own_cnp_list[x] == foreign_cnp_list[x]):
            score += 20

    return score
