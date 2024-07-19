# Overview

As a software engineer, I developed a Health and Fitness Tracker to further my learning and enhance my skills in cloud database, specifically focusing on integrating a Google Firebase cloud database with a Flask web application. This project allows users/physicians to manage their health and fitness activities, including adding, updating, and deleting activities associated with their profiles. The software constains comments for easy understanding, integrates seamlessly with Firebase Firestore, a cloud-based NoSQL database, to store and manage user data and activities.

The purpose of this software is to provide a challenge for me to learn other cloud database other than MongoDB. It demonstrates the integration of front-end and back-end technologies, as well as cloud database management.

[Software Demo Video](https://youtu.be/NPfK5rBv_os)

# Cloud Database

The cloud database used in this project is Firebase Firestore. Firestore is a flexible, scalable database for mobile, web, and server development. It provides real-time data synchronization and offline support.

The database structure includes two main collections:
- **users**: This collection stores user profiles, including their unique IDs, names, and email addresses.
- **activities**: This collection stores activity records associated with user IDs, including activity types and durations.

# Development Environment

The development environment for this project includes the following tools:
- **Visual Studio Code**: An integrated development environment (IDE)
- **Flask**: A lightweight WSGI web application framework used to develop the server-side logic.
- **Firebase Admin SDK**: Used for authentication and managing Firestore database operations.

The primary programming language used is Python, with additional HTML and CSS for front-end development. The Flask framework and Firebase Admin SDK are the main libraries i used in this project.

# Useful Websites

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Firebase Documentation](https://firebase.google.com/docs)
- [Creating a Service Account on Firebase Console](https://cloud.google.com/docs/authentication/getting-started)
- [Don't add Google Service JSON to Your Public Repositore - Stack Overflow](https://stackoverflow.com/questions/37358340/should-i-add-the-google-services-json-from-firebase-to-my-repository?r=SearchResults&s=3%7C88.5889)
- [Python + Firebase (Pyrebase) CRUD Tutorials - YOUTUBE](https://www.youtube.com/watch?v=LaGYxQWYmmc&list=PLs3IFJPw3G9Jwaimh5yTKot1kV5zmzupt)
- [Connecting Firebase Realtime Database To Python: Creating, Reading, Updating, and Deleting Data](https://www.youtube.com/watch?v=DCaH4bQ4DxA&pp=ygUoaG93IHRvIHNldHVwIGdvb2dsZSBmaXJlYmFzZSB3aXRoIHB5dGhvbg%3D%3D)

# Future Work

- Add more detailed health metrics and analytics for users.
- Improve the UI/UX design for a more interactive, responsive user experience.
- Implement unit, integration, and end-to-end tests to ensure the reliability of the application.
- Include functionality to include social features, such as sharing activities and achievements with friends.
