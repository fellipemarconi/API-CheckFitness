from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
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
    
class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsPersonalOrReadOnly, ]
    filter_backends = [SearchFilter]
    search_fields = ['email', 'name']
    
    def get_queryset(self):
        queryset = Student.objects.all().filter(student_personal=self.request.user)
        if queryset:
            return queryset
        else:
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