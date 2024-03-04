from django.core import exceptions
from django.contrib.auth import password_validation
from django.db import transaction

from rest_framework import serializers
from ..models import Personal, Student


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = (
                'id', 'username', 'first_name', 
                'last_name', 'email', 'is_personal',
                'password',
    )
        extra_kwargs = {
            'is_personal': {'read_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
        }
    
    @transaction.atomic()
    def create(self, validated_data):
        user = Personal(**validated_data)
        password = validated_data.get('password')
        user.set_password(password)
        
        user.save()
        return user
    
    def validate_email(self, value):
        email = value
        
        if Personal.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email is already registered', code='invalid')
        
        return email
    
    def validate_password(self, data):
        try:
            password_validation.validate_password(password=data, user=data)
            
        except exceptions.ValidationError as e:
            errors = list(e.messages)
            raise serializers.ValidationError(errors)
        
        return data

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
                'id', 'username', 'first_name', 
                'last_name', 'email', 'age', 
                'height', 'weight', 'password',
    )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
        }
    
    @transaction.atomic()
    def create(self, validated_data):
        user = Student(**validated_data)
        password = validated_data.get('password')
        user.set_password(password)
        
        user.save()
        return user
    
    def validate_email(self, value):
        email = value
        
        if Student.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email is already registered', code='invalid')
        
        return email
    
    def validate_password(self, data):
        try:
            password_validation.validate_password(password=data, user=data)
            
        except exceptions.ValidationError as e:
            errors = list(e.messages)
            raise serializers.ValidationError(errors)
        
        return data