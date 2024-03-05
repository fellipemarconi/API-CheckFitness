from django.db import models
from django.contrib.auth.models import User



class SexOptions(models.TextChoices):
    FEMALE = ('F', 'Female')
    MALE = ('M', 'Male')
    UNSURE = ('U', 'Unsure')

class Personal(User):
    
    is_personal = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personais'
    
    def __str__(self) -> str:
        return self.username
    
class Student(User):
    height = models.FloatField()
    weight = models.FloatField()
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SexOptions.choices)
    student_personal = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    
    def __str__(self) -> str:
        return self.username