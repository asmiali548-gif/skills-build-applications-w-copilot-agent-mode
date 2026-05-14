from django.contrib import admin
from .models import Profile, Activity, Team, Leaderboard, WorkoutSuggestion, TeamMember

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'bio', 'height', 'weight']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'activity_type', 'duration', 'calories_burned', 'date']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['team_id', 'user_id']

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['team_id', 'user_id', 'total_calories', 'rank']

@admin.register(WorkoutSuggestion)
class WorkoutSuggestionAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'suggestion', 'created_at']