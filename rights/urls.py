from django.urls import path

from . import views


urlpatterns = [
    path('right/<int:pk>', views.RightView.as_view()),
    path('rights/tags/', views.TagList.as_view()),
    path('rights/', views.RightList.as_view()),
]
