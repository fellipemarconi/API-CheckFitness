from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from .serializers import StudentSerializer, PersonalSerializer
from ..models import Personal, Student
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PersonalViewSet(ModelViewSet):
    serializer_class = PersonalSerializer
    
    def get_queryset(self):
        queryset = Personal.objects.filter(username=self.request.user.username) # type:ignore
        return queryset
    
class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    
    def get_queryset(self):
        queryset = Student.objects.filter(username=self.request.user.username) # type:ignore
        return queryset