from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail

from django_rest_passwordreset.signals import reset_password_token_created


class SexOptions(models.TextChoices):
    FEMALE = ('F', 'Female')
    MALE = ('M', 'Male')
    OTHER = ('O', 'Other')
    
class Sport(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class Personal(User):
    name = models.CharField(max_length=255)
    is_personal = models.BooleanField(default=True)
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personais'
    
    def __str__(self) -> str:
        return self.username
    
    @receiver(reset_password_token_created)
    def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
        email_plaintext_message = "Open the link to reset your password:" + " " + "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key)
        
        send_mail(
            "Password Reset for {title}".format(title="CheckFitness account"),
            email_plaintext_message,
            "info@yourcompany.com",
            [reset_password_token.user.email],
            fail_silently=False,
        )
    
class Student(User):
    name = models.CharField(max_length=255)
    height = models.FloatField()
    weight = models.FloatField()
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SexOptions.choices)
    student_personal = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True)
    sport = models.ManyToManyField(Sport, blank=True)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    
    def __str__(self) -> str:
        return self.username
    
    @receiver(reset_password_token_created)
    def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
        email_plaintext_message = "Open the link to reset your password:" + " " + "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key)
        
        send_mail(
            "Password Reset for {title}".format(title="CheckFitness account"),
            email_plaintext_message,
            "info@yourcompany.com",
            [reset_password_token.user.email],
            fail_silently=False,
        )