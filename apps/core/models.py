from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Personal(User):
    
    is_personal = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personais'
    
    def __str__(self) -> str:
        return self.username
    
class Student(User):
    height = models.FloatField(blank=True)
    weight = models.FloatField(blank=True)
    age = models.IntegerField()
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    
    def __str__(self) -> str:
        return self.username