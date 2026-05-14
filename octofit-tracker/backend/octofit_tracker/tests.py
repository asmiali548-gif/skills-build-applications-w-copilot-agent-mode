from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Activity, Team

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile.objects.create(user_id=self.user.id, bio='Test bio')

    def test_profile_creation(self):
        self.assertEqual(self.profile.user_id, self.user.id)
        self.assertEqual(self.profile.bio, 'Test bio')

class ActivityTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.activity = Activity.objects.create(
            user_id=self.user.id,
            activity_type='Running',
            duration=30,
            calories_burned=300
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.user_id, self.user.id)
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)

class TeamTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='A test team')

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.description, 'A test team')