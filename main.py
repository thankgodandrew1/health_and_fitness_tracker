from auth import initialize_firebase, create_user, delete_user
from db import initialize_firestore, add_user, get_user, update_user, delete_user_data, add_activity, get_activities
# import secrets

def main():

    # secret_key = secrets.token_hex(32)
    # print(secret_key)
    
    # initializes both Firebase and Firestore
    initialize_firebase()
    initialize_firestore()
    
    # user authentication
    user_id = create_user('andytester@tester.com', 'password1234')
    if not user_id:
        print("Failed to create user. Exiting.")
        return
    
    # add user data
    add_user(user_id, 'Tester Andrew', 'andytester@tester.com')
    
    # Add activity data
    add_activity(user_id, 'Jumping', 30)
    add_activity(user_id, 'Swimming', 45)
    add_activity(user_id, 'Hiking', 30)
    add_activity(user_id, 'Running', 20)
    add_activity(user_id, 'Cycling', 35)
    
    # Retrieve user data
    user_data = get_user(user_id)
    
    # Retrieve activities
    activities = get_activities(user_id)
    
    # Update user data
    update_user(user_id, {'name': 'Updated Test Andy'})
    
    # update activity data
    # just here, assuming we know the activity_id (retrieved from get_activities)
    # activity_id = activities[0]['activity_id']
    # update_activity(activity_id, {'duration': 60})
    
    # we could delete activity data by calling on the delete_activity function and pass the id 
    # delete_activity(activity_id)
    
    # same with deleting user data call the function and pass in the user's id from the firestore db
    # delete_user_data(user_id)
    
    # same with deleting the auth. user from the firebase console 
    # Delete user authentication
    # delete_user(user_id)

if __name__ == '__main__':
    main()