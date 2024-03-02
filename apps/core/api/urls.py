from rest_framework import routers
from .views import StudentViewSet, PersonalViewSet


router = routers.SimpleRouter()
router.register(r'personal', PersonalViewSet, basename='personal')
router.register(r'student', StudentViewSet, basename='student')


urlpatterns = router.urls