from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Company
from .serializers import CompanySerializer, UserSerializer
from datetime import datetime

from django.contrib.auth import (login as auth_login,  authenticate)
from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User


def login(request):
    """
    Login to app.
    """
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'my_crm/login.html', context)


@csrf_exempt
def companies_list(request):
    """
    List all companies.
    """
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def companies_create(request):
    """
    Create a new company.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = User.objects.get(pk=data['user_id'])
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def users_list(request):
    """
    List all users.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def user_detail(request, pk):
    """
    Detail user.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)