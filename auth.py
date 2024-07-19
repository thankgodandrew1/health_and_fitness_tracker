# imports firebase_admin to hNDLE USER authentications 
import firebase_admin
from firebase_admin import credentials, auth

# initializes Firebasee
def initialize_firebase():
    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate('config/health_and_fitness_tracker.json')
            firebase_admin.initialize_app(cred)
        print("Firebase initialized successfully")
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
# function to create users... i initially specied the email/password sign in method on Firebase Console
def create_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        print(f'Successfully created user: {user.uid}')
        return user.uid
    except Exception as e:
        print(f"Error creating user: {e}")
        return None

# func to delete authenticated users
def delete_user(uid):
    try:
        auth.delete_user(uid)
        print(f'Successfully deleted user: {uid}')
    except Exception as e:
        print(f"Error deleting user: {e}")

# funtion to handle users information update
def update_user(uid, email=None, password=None):
    try:
        user = auth.update_user(
            uid,
            email=email,
            password=password
        )
        print(f'Successfully updated user: {user.uid}')
    except Exception as e:
        print(f"Error updating user: {e}")
