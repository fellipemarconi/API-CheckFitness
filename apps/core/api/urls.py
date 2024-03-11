from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register(r'personal', views.PersonalViewSet, basename='personal')
router.register(r'student', views.StudentViewSet, basename='student')


urlpatterns = router.urls