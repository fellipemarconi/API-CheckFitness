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