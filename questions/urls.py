from rest_framework.routers import DefaultRouter

from .views import ListCreateQuestionsViewSet

router = DefaultRouter()
router.register(r'questions', ListCreateQuestionsViewSet, basename='questions')
