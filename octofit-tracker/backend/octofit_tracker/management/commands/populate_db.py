from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Populates the database with test data'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        
        User.objects.create_user(username='thundergod', email='thundergod@octofit.com', password='password')
        User.objects.create_user(username='metalgeek', email='metalgeek@octofit.com', password='password')
        User.objects.create_user(username='zerocool', email='zerocool@octofit.com', password='password')
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with test users'))