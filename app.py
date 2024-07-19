# imports essential modules
from flask import Flask, render_template, request, redirect, url_for, flash
from firebase_admin import credentials, firestore, initialize_app
import auth
import db

app = Flask(__name__)
app.config.from_object('config.Config')

# initializes the Firebase cloud platform with its credentials specified in the config folder
cred = credentials.Certificate('config/health_and_fitness_tracker.json')
initialize_app(cred)
db.initialize_firestore()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

# gets user page to display on browseer
@app.route('/users')
def users():
    users_list = db.get_users()
    return render_template('user.html', users=users_list)

# route to add users both on firebase and our database
@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    user_id = auth.create_user(email, password)
    if user_id:
        db.add_user(user_id, name, email)
        flash('User added successfully!')
    else:
        flash('Error adding user.')
    return redirect(url_for('users'))

# route to delete users both on our cloud db and firebase console
@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    auth.delete_user(user_id)
    db.delete_user_data(user_id)
    flash('User deleted successfully!')
    return redirect(url_for('users'))

# handles users update
@app.route('/update_user/<user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        update_data = {'name': name, 'email': email}
        db.update_user(user_id, update_data)
        auth.update_user(user_id, email=email)
        flash('User updated successfully!')
        return redirect(url_for('users'))
    else:
        user = db.get_user(user_id)
        if user:
            user['id'] = user_id
            return render_template('update_user.html', user=user)
        else:
            flash('User not found!')
            return redirect(url_for('users'))

# routes  for managing activities
# route to get activities associated to a user
@app.route('/activities/<user_id>')
def activities(user_id):
    user = db.get_user(user_id)
    # check if users exists if not redirects to the users page
    if not user:
        flash('User not found!')
        return redirect(url_for('users'))
    
    activities_list = db.get_activities(user_id)
    return render_template('activities.html', user_id=user_id, user_name=user['name'], activities=activities_list)

# route to create activities for users
@app.route('/add_activity/<user_id>', methods=['POST'])
def add_activity(user_id):
    activity_type = request.form['activity_type']
    duration = request.form['duration']
    db.add_activity(user_id, activity_type, duration)
    flash('Activity added successfully!')
    return redirect(url_for('activities', user_id=user_id))

# handles activities deletion process
@app.route('/delete_activity/<activity_id>/<user_id>')
def delete_activity(activity_id, user_id):
    db.delete_activity(activity_id)
    flash('Activity deleted successfully!')
    return redirect(url_for('activities', user_id=user_id))

@app.route('/update_activity/<activity_id>/<user_id>', methods=['GET', 'POST'])
def update_activity(activity_id, user_id):
    # print(f"Update activity called with activity_id={activity_id} and user_id={user_id}")
    if request.method == 'POST':
        activity_type = request.form['activity_type']
        duration = request.form['duration']
        update_data = {'activity_type': activity_type, 'duration': duration}
        db.update_activity(activity_id, update_data)
        flash('Activity updated successfully!')
        return redirect(url_for('activities', user_id=user_id))
    else:
        activity = db.get_activity(activity_id)
        if activity:
            return render_template('update_activity.html', activity=activity, user_id=user_id)
        else:
            flash('Activity not found!')
            return redirect(url_for('activities', user_id=user_id))



if __name__ == '__main__':
    # call on flask debug feature set it to true
    app.run(debug=True)
