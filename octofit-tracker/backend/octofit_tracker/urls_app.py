from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'leaderboards', views.LeaderboardViewSet)
router.register(r'workout-suggestions', views.WorkoutSuggestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]