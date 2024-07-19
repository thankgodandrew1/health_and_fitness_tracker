#import essentials from the firebase_admin package
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# initializes our db
db = None

# initialize firestore to store users info
def initialize_firestore():
    try:
        global db
        if not firebase_admin._apps:
            cred = credentials.Certificate('config/health_and_fitness_tracker.json')
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        print("Firestore initialized successfully")
    # handle exceptions by throwing errs to the console if connection fails    
    except Exception as e:
        print(f"Error initializing Firestore: {e}")

# CRUD operations for users
# handles addition of users to the user collection in our firestore db
def add_user(user_id, name, email):
    user_ref = db.collection('users').document(user_id)
    user_ref.set({
        'name': name,
        'email': email,
        'created_at': datetime.now()
    })
    print(f'User {name} added to Firestore')

# retrieves a specific user by their ID
def get_user(user_id):
    # access the database
    user_ref = db.collection('users').document(user_id)
    user = user_ref.get()

    # check if the user with the specified id exists in the database
    if user.exists:
        # print the user data 
        print(f'User data: {user.to_dict()}')
        return user.to_dict()
    else:
        # print this
        print(f'No such user: {user_id}')
        return None

# update a user funtions
def update_user(user_id, update_data):
    user_ref = db.collection('users').document(user_id)
    user_ref.update(update_data)
    print(f'User {user_id} updated with {update_data}')

def delete_user_data(user_id):
    user_ref = db.collection('users').document(user_id)
    user_ref.delete()
    print(f'User {user_id} deleted from Firestore')

# funtion to get the whole users from the db
def get_users():
    # get into the users collection in the database
    users_ref = db.collection('users')
    users = users_ref.stream()
    # pass the users into a list
    users_list = []
    # iterate through the loop and add each user to the user_list to return to the UI
    for user in users:
        user_data = user.to_dict()
        user_data['id'] = user.id
        users_list.append(user_data)
    return users_list

# CRUD operations for activities

# function for adding activities to the db parameter are user id, the type of activity, timestamp(creation time), and the duration of the activity
def add_activity(user_id, activity_type, duration):
    activity_ref = db.collection('activities').document()
    activity_ref.set({
        'user_id': user_id,
        'activity_type': activity_type,
        'duration': duration,
        'timestamp': datetime.now()
    })
    # print(f'Activity added for user {user_id}')

# gets all activities tied to a user
def get_activities(user_id):
    activities_ref = db.collection('activities')
    query = activities_ref.where('user_id', '==', user_id).stream()
    activities = []
    for activity in query:
        activity_data = activity.to_dict()
        activity_data['id'] = activity.id
        activities.append(activity_data)
    print(f'Activities for user {user_id}: {activities}')
    return activities

#  gets a single activity by its id
def get_activity(activity_id):
    activity_ref = db.collection('activities').document(activity_id)
    activity = activity_ref.get()
    if activity.exists:
        print(f'Activity data: {activity.to_dict()}')
        return activity.to_dict()
    else:
        print(f'No such activity: {activity_id}')
        return None

# updates
def update_activity(activity_id, update_data):
    activity_ref = db.collection('activities').document(activity_id)
    activity_ref.update(update_data)
    print(f'Activity {activity_id} updated with {update_data}')

# deletes activities
def delete_activity(activity_id):
    activity_ref = db.collection('activities').document(activity_id)
    activity_ref.delete()
    print(f'Activity {activity_id} deleted from Firestore')
