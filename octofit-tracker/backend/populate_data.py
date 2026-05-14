import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from django.contrib.auth.models import User
from octofit_tracker.models import Profile, Activity, Team, Leaderboard, WorkoutSuggestion

# Create users
user1 = User.objects.create_user(username='alice', email='alice@example.com', password='pass123', first_name='Alice', last_name='Smith')
user2 = User.objects.create_user(username='bob', email='bob@example.com', password='pass123', first_name='Bob', last_name='Johnson')
user3 = User.objects.create_user(username='charlie', email='charlie@example.com', password='pass123', first_name='Charlie', last_name='Brown')

# Create profiles
Profile.objects.create(user=user1, bio='Fitness enthusiast', height=165, weight=60, fitness_goals='Lose 5kg')
Profile.objects.create(user=user2, bio='Marathon runner', height=180, weight=75, fitness_goals='Run a marathon')
Profile.objects.create(user=user3, bio='Weight lifter', height=175, weight=80, fitness_goals='Gain muscle')

# Create activities
Activity.objects.create(user=user1, activity_type='Running', duration=30, calories_burned=300, notes='Morning run')
Activity.objects.create(user=user1, activity_type='Cycling', duration=45, calories_burned=400, notes='Evening ride')
Activity.objects.create(user=user2, activity_type='Running', duration=60, calories_burned=600, notes='Long run')
Activity.objects.create(user=user3, activity_type='Weightlifting', duration=50, calories_burned=250, notes='Upper body day')

# Create team
team = Team.objects.create(name='FitTeam', description='A team for fitness lovers')
team.members.add(user1, user2, user3)

# Create leaderboard
Leaderboard.objects.create(team=team, user=user1, total_calories=700, rank=1)
Leaderboard.objects.create(team=team, user=user2, total_calories=600, rank=2)
Leaderboard.objects.create(team=team, user=user3, total_calories=250, rank=3)

# Create workout suggestions
WorkoutSuggestion.objects.create(user=user1, suggestion='Try HIIT workouts for better calorie burn')
WorkoutSuggestion.objects.create(user=user2, suggestion='Incorporate hill runs to build endurance')
WorkoutSuggestion.objects.create(user=user3, suggestion='Focus on compound lifts for overall strength')

print("Test data populated successfully!")