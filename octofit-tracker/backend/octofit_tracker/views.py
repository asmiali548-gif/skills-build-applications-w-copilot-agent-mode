from rest_framework import viewsets, permissions
from .models import Profile, Activity, Team, Leaderboard, WorkoutSuggestion
from .serializers import ProfileSerializer, ActivitySerializer, TeamSerializer, LeaderboardSerializer, WorkoutSuggestionSerializer
from django.contrib.auth.models import User

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Profile.objects.filter(user_id=self.request.user.id)
        return Profile.objects.all()

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Activity.objects.filter(user_id=self.request.user.id)
        return Activity.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class WorkoutSuggestionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSuggestion.objects.all()
    serializer_class = WorkoutSuggestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return WorkoutSuggestion.objects.filter(user_id=self.request.user.id)
        return WorkoutSuggestion.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)