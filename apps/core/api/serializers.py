from django.core import exceptions
from django.contrib.auth import password_validation
from django.db import transaction
from django.contrib.auth.models import User

from rest_framework import serializers
from ..models import Personal, Student


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = (
                'id', 'username', 'email', 'name', 
                'is_personal', 'password',
    )
        extra_kwargs = {
            'email': {'required': True},
            'is_personal': {'read_only': True},
            'username': {'read_only': True},
        }
    
    @transaction.atomic()
    def create(self, validated_data):
        user = Personal(**validated_data, username=validated_data['email'])
        password = validated_data.get('password')
        user.set_password(password)
        
        user.save()
        return user
    
    def validate_email(self, value):
        email = value
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email is already registered', code='invalid')
        
        if email == '':
            raise serializers.ValidationError('Email cannot be null or empty', code='invalid')
        
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
                'id', 'username', 'email', 
                'name', 'age', 'height', 
                'weight', 'sex', 'student_personal', 
                'password',
    )
        extra_kwargs = {
            'email': {'required': True},
            'username': {'read_only': True},
            'student_personal': {'read_only': True}
        }
    
    @transaction.atomic()
    def create(self, validated_data):
        student_personal = Personal.objects.filter(username=self.context['request'].user).first()
        
        user = Student(**validated_data, student_personal=student_personal, username=validated_data['email'])
        password = validated_data.get('password')
        user.set_password(password)
        
        user.save()
        return user
    
    def validate_email(self, value):
        email = value
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email is already registered', code='invalid')
        
        if email == '':
            raise serializers.ValidationError('Email cannot be null or empty', code='invalid')
        
        return email
    
    def validate_password(self, data):
        try:
            password_validation.validate_password(password=data, user=data)
            
        except exceptions.ValidationError as e:
            errors = list(e.messages)
            raise serializers.ValidationError(errors)
        
        return data