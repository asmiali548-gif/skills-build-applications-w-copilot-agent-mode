from rest_framework import serializers
from .models import Profile, Activity, Team, Leaderboard, WorkoutSuggestion
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['_id', 'user_id', 'username', 'bio', 'date_of_birth', 'height', 'weight', 'fitness_goals']

    def get_username(self, obj):
        try:
            user = User.objects.get(id=obj.user_id)
            return user.username
        except User.DoesNotExist:
            return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance._id:
            representation['id'] = str(instance._id)
        return representation

class ActivitySerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['_id', 'user_id', 'username', 'activity_type', 'duration', 'calories_burned', 'date', 'notes']

    def get_username(self, obj):
        try:
            user = User.objects.get(id=obj.user_id)
            return user.username
        except User.DoesNotExist:
            return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance._id:
            representation['id'] = str(instance._id)
        return representation

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name', 'description', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance._id:
            representation['id'] = str(instance._id)
        return representation

class LeaderboardSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    team_name = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['_id', 'team_id', 'team_name', 'user_id', 'username', 'total_calories', 'rank']

    def get_username(self, obj):
        try:
            user = User.objects.get(id=obj.user_id)
            return user.username
        except User.DoesNotExist:
            return None

    def get_team_name(self, obj):
        try:
            team = Team.objects.get(_id=obj.team_id)
            return team.name
        except Team.DoesNotExist:
            return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance._id:
            representation['id'] = str(instance._id)
        return representation

class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = WorkoutSuggestion
        fields = ['_id', 'user_id', 'username', 'suggestion', 'created_at']

    def get_username(self, obj):
        try:
            user = User.objects.get(id=obj.user_id)
            return user.username
        except User.DoesNotExist:
            return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance._id:
            representation['id'] = str(instance._id)
        return representation