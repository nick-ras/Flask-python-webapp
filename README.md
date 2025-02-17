# Flask Web Application for Box Booking

This is a Flask-based web application designed for users to book boxes for storage, package pickup, or other similar use cases. The application features a user authentication system, dynamic webpage interactions, and a secure environment for both users and data.

## Features

- **User Authentication**: Users can securely log in to the system, manage their bookings, and track reservations.
- **Box Booking**: Users can book boxes for a duration ranging from 6 to 48 hours.
- **Dynamic Webpages**: Using JQuery, the frontend is designed to provide a smooth user experience with real-time updates.
- **Security**: 
  - **SQL Injection Protection**: The application uses **SQLAlchemy** to interact with the database, which prevents SQL injection attacks by automatically escaping user inputs.
  - **CSRF Protection**: Flask-WTF is used to ensure all form submissions are secured against Cross-Site Request Forgery (CSRF) attacks.
  - **Session Management**: Flask handles user sessions securely, ensuring that user data is stored in a way that prevents session hijacking and fixation.
  - **Basic Authentication**: Passwords are securely handled, and user credentials are stored with secure hashing techniques (though more advanced hashing techniques can be added based on needs).

## Architecture

The application uses a database with two main tables:
- **Users Table**: Stores user credentials, including hashed passwords, and user data.
- **Boxes Table**: Stores information about available boxes and booking details.

## Setup Instructions

### Requirements

- Python 3.x
- A database server running Microsoft SQL Server (ODBC driver required).
