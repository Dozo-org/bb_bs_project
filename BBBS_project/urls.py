from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

from afisha.routers import CustomRouter
from afisha.urls import router as afisha_router
from common.urls import router as common_router
from places.urls import router as places_router
from places.views import PlaceRetreiveUpdate

v1_router = DefaultRouter() # TODO: remove customrouter
v1_router.registry.extend(afisha_router.registry)
v1_router.registry.extend(common_router.registry)
v1_router.registry.extend(places_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(v1_router.urls)),
    path('api/v1/place/', PlaceRetreiveUpdate.as_view()),
]
