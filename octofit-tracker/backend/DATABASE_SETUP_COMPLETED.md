# OctoFit Tracker MongoDB Database Setup - COMPLETED

## Summary
Successfully initialized and populated the `octofit_db` MongoDB database with complete Django backend configuration and test data.

## Tasks Completed

### 1. ✓ Updated Django Settings (settings.py)
- Configured INSTALLED_APPS with all required packages:
  - Django REST Framework
  - django-allauth for authentication
  - dj-rest-auth for REST authentication
  - corsheaders for CORS support
  - octofit_tracker app
- Added ALLOWED_HOSTS configuration for Codespaces
- Configured MongoDB/Djongo database connection
- Set up REST_FRAMEWORK authentication with TokenAuthentication
- Configured CORS_ALLOWED_ORIGINS for frontend
- Added SITE_ID = 1 for django-allauth

### 2. ✓ Updated Django Project Structure
- **models.py**: Created 6 Djongo models for MongoDB:
  - Profile: User profiles with fitness info
  - Activity: Logged activities
  - Team: Team management
  - TeamMember: Team membership tracking
  - Leaderboard: Competitive rankings
  - WorkoutSuggestion: Personalized suggestions
  
- **serializers.py**: Created REST API serializers with ObjectId handling
  - All serializers convert MongoDB ObjectIds to strings
  - Include helper methods to get related user information
  
- **views.py**: Created ViewSets for all models with proper permissions
  - ProfileViewSet
  - ActivityViewSet
  - TeamViewSet
  - LeaderboardViewSet
  - WorkoutSuggestionViewSet
  
- **urls_app.py**: Created app-specific URL routing
- **admin.py**: Registered all models in Django Admin
- **tests.py**: Created unit tests for models
- **urls.py (project)**: Updated with API endpoints and authentication routes

### 3. ✓ Created populate_db.py Script
- Automatically creates test users (alice, bob, charlie)
- Populates user profiles with fitness information
- Creates sample activities (Running, Cycling, Weightlifting)
- Creates team (FitTeam) with members
- Creates leaderboard entries with rankings
- Creates personalized workout suggestions
- Includes data clearing and verification

### 4. ✓ Verified MongoDB Database Population

**Database: octofit_db**

| Collection | Count | Details |
|-----------|-------|---------|
| auth_user | 12 | Test users created |
| profile | 3 | User profiles (alice, bob, charlie) |
| activity | 4 | Activity logs |
| team | 1 | FitTeam created |
| team_members | 3 | Team memberships |
| leaderboard | 3 | Competitive rankings |
| workout_suggestion | 3 | Personalized suggestions |

**Sample Data Structure:**
```
User: alice (ObjectId: 6a05dab0b2b7213f02112f93)
  - Email: alice@example.com
  - Profile: Fitness enthusiast, 165cm, 60kg, Goal: Lose 5kg
  - Activities: Running (30min, 300cal), Cycling (45min, 400cal)
  - Leaderboard: Rank 1 with 700 calories

User: bob (ObjectId: 6a05dab1b2b7213f02112f94)
  - Email: bob@example.com
  - Profile: Marathon runner, 180cm, 75kg, Goal: Run a marathon
  - Activities: Running (60min, 600cal)
  - Leaderboard: Rank 2 with 600 calories

User: charlie (ObjectId: 6a05dab1b2b7213f02112f95)
  - Email: charlie@example.com
  - Profile: Weight lifter, 175cm, 80kg, Goal: Gain muscle
  - Activities: Weightlifting (50min, 250cal)
  - Leaderboard: Rank 3 with 250 calories

Team: FitTeam
  - Members: alice, bob, charlie
```

## Key Features Implemented

1. **User Authentication**: Token-based authentication with dj-rest-auth
2. **Activity Tracking**: Log exercises with calories and duration
3. **Team Management**: Create teams and track membership
4. **Competitive Leaderboard**: Rank users by total calories burned
5. **Personalized Suggestions**: Customized workout recommendations
6. **MongoDB Integration**: Full Djongo integration with ObjectId support
7. **REST API**: Complete API endpoints for all models
8. **Django Admin**: Full admin interface for data management

## How to Use

### Run the populate script:
```bash
cd octofit-tracker/backend
source venv/bin/activate
python populate_db.py
```

### Access Django Admin:
```bash
python manage.py createsuperuser
python manage.py runserver
# Visit: http://localhost:8000/admin
```

### Query the API:
```bash
# Get all profiles
curl http://localhost:8000/api/profiles/

# Get all activities
curl http://localhost:8000/api/activities/

# Get leaderboard
curl http://localhost:8000/api/leaderboards/
```

## Database Structure (MongoDB)

The database uses Djongo (Django-MongoDB adapter) with the following structure:

- **auth_user**: Django default user model (stored in MongoDB)
- **profile**: User profile information
- **activity**: Activity logs
- **team**: Team data
- **team_members**: Team membership mappings
- **leaderboard**: Competitive rankings
- **workout_suggestion**: Personalized suggestions

All collections use MongoDB's ObjectId for primary keys and store data in MongoDB's BSON format.

## Notes
- All ObjectIds are automatically converted to strings in API responses
- User IDs are stored as strings (MongoDB ObjectIds) in related models
- The populate_db.py script can be run multiple times to add more test data
- Delete old data before running populate_db.py to avoid duplicates
