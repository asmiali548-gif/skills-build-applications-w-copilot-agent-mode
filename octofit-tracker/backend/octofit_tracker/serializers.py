from rest_framework import serializers
from .models import Profile, Activity, Team, Leaderboard, WorkoutSuggestion
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'date_of_birth', 'height', 'weight', 'fitness_goals']

class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'calories_burned', 'date', 'notes']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if hasattr(instance, '_id') and instance._id:
            representation['id'] = str(instance._id)
        return representation

class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'members', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if hasattr(instance, '_id') and instance._id:
            representation['id'] = str(instance._id)
        return representation

class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'user', 'total_calories', 'rank']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if hasattr(instance, '_id') and instance._id:
            representation['id'] = str(instance._id)
        return representation

class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = WorkoutSuggestion
        fields = ['id', 'user', 'suggestion', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if hasattr(instance, '_id') and instance._id:
            representation['id'] = str(instance._id)
        return representation