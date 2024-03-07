from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

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
    
    def update(self, request, pk=None, *args, **kwargs):
        student = Student.objects.filter(pk=pk, student_personal=request.user).first()
        try:
            serializer = self.get_serializer(student, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except:
            return Response({'message': 'You dont have permission to update this student.'}, status=status.HTTP_403_FORBIDDEN)
    
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            errors = list(e.args)
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)