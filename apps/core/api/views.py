from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import StudentSerializer, PersonalSerializer
from ..models import Personal, Student
from ..permissions import IsPersonalOrReadOnly


class PersonalViewSet(ModelViewSet):
    serializer_class = PersonalSerializer
    
    def get_queryset(self):
        queryset = Personal.objects.filter(username=self.request.user.username) # type:ignore
        return queryset
    
    @action(methods=['get'], detail=False)
    def my_students(self, request):
        students = Student.objects.filter(student_personal=request.user)
        serializer = StudentSerializer(instance=students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsPersonalOrReadOnly, ]
    
    def get_queryset(self):
        queryset = Student.objects.filter(username=self.request.user.username) # type:ignore
        return queryset