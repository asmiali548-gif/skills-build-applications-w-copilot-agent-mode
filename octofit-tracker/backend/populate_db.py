#!/usr/bin/env python
"""
Script to populate the octofit_db MongoDB database with test data.
"""
import os
import sys
import django

# Add the backend directory to the path
sys.path.insert(0, os.path.dirname(__file__))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from django.contrib.auth.models import User
from octofit_tracker.models import Profile, Activity, Team, Leaderboard, WorkoutSuggestion, TeamMember

def main():
    print("Starting database population...")
    
    # Clear existing data (bypass cascade issues with Djongo)
    print("Clearing existing data...")
    try:
        WorkoutSuggestion.objects.all().delete()
        Leaderboard.objects.all().delete()
        TeamMember.objects.all().delete()
        Activity.objects.all().delete()
        Profile.objects.all().delete()
        Team.objects.all().delete()
        print("✓ Existing data cleared")
    except Exception as e:
        print(f"Warning: Could not clear all data: {e}")
        print("Continuing with population...")
    
    # Create users
    print("Creating users...")
    user1 = User.objects.create_user(
        username='alice',
        email='alice@example.com',
        password='pass123',
        first_name='Alice',
        last_name='Smith'
    )
    user2 = User.objects.create_user(
        username='bob',
        email='bob@example.com',
        password='pass123',
        first_name='Bob',
        last_name='Johnson'
    )
    user3 = User.objects.create_user(
        username='charlie',
        email='charlie@example.com',
        password='pass123',
        first_name='Charlie',
        last_name='Brown'
    )
    print(f"✓ Users created: alice (id={user1.id}), bob (id={user2.id}), charlie (id={user3.id})")
    
    # Create profiles
    print("Creating profiles...")
    Profile.objects.create(
        user_id=str(user1.id),
        bio='Fitness enthusiast',
        height=165,
        weight=60,
        fitness_goals='Lose 5kg'
    )
    Profile.objects.create(
        user_id=str(user2.id),
        bio='Marathon runner',
        height=180,
        weight=75,
        fitness_goals='Run a marathon'
    )
    Profile.objects.create(
        user_id=str(user3.id),
        bio='Weight lifter',
        height=175,
        weight=80,
        fitness_goals='Gain muscle'
    )
    print("✓ Profiles created")
    
    # Create activities
    print("Creating activities...")
    Activity.objects.create(
        user_id=str(user1.id),
        activity_type='Running',
        duration=30,
        calories_burned=300,
        notes='Morning run'
    )
    Activity.objects.create(
        user_id=str(user1.id),
        activity_type='Cycling',
        duration=45,
        calories_burned=400,
        notes='Evening ride'
    )
    Activity.objects.create(
        user_id=str(user2.id),
        activity_type='Running',
        duration=60,
        calories_burned=600,
        notes='Long run'
    )
    Activity.objects.create(
        user_id=str(user3.id),
        activity_type='Weightlifting',
        duration=50,
        calories_burned=250,
        notes='Upper body day'
    )
    print("✓ Activities created")
    
    # Create team
    print("Creating team...")
    team = Team.objects.create(
        name='FitTeam',
        description='A team for fitness lovers'
    )
    print(f"✓ Team created: FitTeam (id={team._id})")
    
    # Add team members
    TeamMember.objects.create(team_id=str(team._id), user_id=str(user1.id))
    TeamMember.objects.create(team_id=str(team._id), user_id=str(user2.id))
    TeamMember.objects.create(team_id=str(team._id), user_id=str(user3.id))
    print("✓ Team members added")
    
    # Create leaderboard
    print("Creating leaderboard...")
    Leaderboard.objects.create(
        team_id=str(team._id),
        user_id=str(user1.id),
        total_calories=700,
        rank=1
    )
    Leaderboard.objects.create(
        team_id=str(team._id),
        user_id=str(user2.id),
        total_calories=600,
        rank=2
    )
    Leaderboard.objects.create(
        team_id=str(team._id),
        user_id=str(user3.id),
        total_calories=250,
        rank=3
    )
    print("✓ Leaderboard created")
    
    # Create workout suggestions
    print("Creating workout suggestions...")
    WorkoutSuggestion.objects.create(
        user_id=str(user1.id),
        suggestion='Try HIIT workouts for better calorie burn'
    )
    WorkoutSuggestion.objects.create(
        user_id=str(user2.id),
        suggestion='Incorporate hill runs to build endurance'
    )
    WorkoutSuggestion.objects.create(
        user_id=str(user3.id),
        suggestion='Focus on compound lifts for overall strength'
    )
    print("✓ Workout suggestions created")
    
    print("\n" + "="*50)
    print("✓ Test data populated successfully!")
    print("="*50)
    print(f"Users: {User.objects.count()}")
    print(f"Profiles: {Profile.objects.count()}")
    print(f"Activities: {Activity.objects.count()}")
    print(f"Teams: {Team.objects.count()}")
    print(f"Team Members: {TeamMember.objects.count()}")
    print(f"Leaderboard entries: {Leaderboard.objects.count()}")
    print(f"Workout suggestions: {WorkoutSuggestion.objects.count()}")
    print("="*50)

if __name__ == '__main__':
    main()
