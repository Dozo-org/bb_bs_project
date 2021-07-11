from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

from common.views import CityViewSet, ProfileViewSet
from afisha.views import EventViewSet, MainViewSet, EventParticipantViewSet
from places.views import PlaceRetrieveCreate, PlacesListViewSet
from questions.views import ListCreateQuestionsViewSet


v1_router = DefaultRouter()
v1_router.register(r'afisha/events', EventViewSet, basename='event')
v1_router.register(r'afisha/event-participants', EventParticipantViewSet,
                basename='event-participant')
v1_router.register(r'main', MainViewSet, basename='main')
v1_router.register(r'cities', CityViewSet, basename='city_list')
v1_router.register(r'profile', ProfileViewSet, basename='profile')
v1_router.register(r'places', PlacesListViewSet, basename='places')
v1_router.register(r'questions', ListCreateQuestionsViewSet, basename='questions')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/place/', PlaceRetrieveCreate.as_view()),
    path('api/v1/', include('rights.urls')),
    path('api/v1/', include(v1_router.urls)),]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

