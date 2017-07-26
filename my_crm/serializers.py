from rest_framework import serializers
from .models import Company

from django.contrib.auth.models import User


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'name', 'email', 'phone_number', 'address', 'code', 'city', 'voivodeship', 'description',
                  'created')


class UserSerializer(serializers.ModelSerializer):
    companies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'is_staff', 'is_active',
                  'is_superuser', 'last_login', 'companies')
