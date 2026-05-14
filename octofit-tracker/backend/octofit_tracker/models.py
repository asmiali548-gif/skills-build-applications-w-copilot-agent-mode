from django.db import models
from django.contrib.auth.models import User
from djongo import models as djongo_models

class Profile(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    user_id = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    fitness_goals = models.TextField(blank=True)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        try:
            user = User.objects.get(id=self.user_id)
            return f"{user.username}'s profile"
        except (User.DoesNotExist, ValueError):
            return f"Profile for user {self.user_id}"

class Activity(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    user_id = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    calories_burned = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'activity'

    def __str__(self):
        try:
            user = User.objects.get(id=self.user_id)
            return f"{user.username} - {self.activity_type} on {self.date}"
        except (User.DoesNotExist, ValueError):
            return f"Activity for user {self.user_id}"

class Team(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'team'

    def __str__(self):
        return self.name

class TeamMember(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    team_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)

    class Meta:
        db_table = 'team_members'

class Leaderboard(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    team_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    total_calories = models.FloatField(default=0)
    rank = models.IntegerField()

    class Meta:
        db_table = 'leaderboard'

    def __str__(self):
        try:
            user = User.objects.get(id=self.user_id)
            return f"{user.username} - Rank {self.rank}"
        except (User.DoesNotExist, ValueError):
            return f"Leaderboard entry for user {self.user_id}"

class WorkoutSuggestion(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    user_id = models.CharField(max_length=100)
    suggestion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'workout_suggestion'

    def __str__(self):
        try:
            user = User.objects.get(id=self.user_id)
            return f"Suggestion for {user.username}"
        except (User.DoesNotExist, ValueError):
            return f"Suggestion for user {self.user_id}"