import re
import bcrypt
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

def is_valid_email(email):
    """
    Check if the given email is valid.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

def is_strong_password(password):
    """
    Check if the given password is strong (e.g., at least 8 characters long).
    """
    return len(password) >= 8

def is_username_available(username):
    """
    Check if the given username is available (not already taken).
    """
    return not User.objects.filter(username=username).exists()
def register_user(request):
    """
    Endpoint for user registration.

    ---
    # Request Body
    {
        "username": "string",
        "email": "string",
        "password": "string"
    }

    # Response
    {
        "message": "User registered successfully!"
    }
    """
    if request.method == 'POST':
        try:
            # Retrieve username, email, and password from the request
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            # Validate email format
            if not is_valid_email(email):
                return JsonResponse({'error': 'Invalid email format'}, status=400)
            
            # Validate password strength
            if not is_strong_password(password):
                return JsonResponse({'error': 'Password must be at least 8 characters long'}, status=400)
            
            # Validate username availability
            if not is_username_available(username):
                return JsonResponse({'error': 'Username is already taken'}, status=400)
            
            # Hash the password using make_password
            hashed_password = make_password(password)
            
            # Now you can save the hashed password to the database
            # Example code to save the hashed password:
            # user = User.objects.create(username=username, email=email, password=hashed_password)
            
            # Return the registration success response
            return JsonResponse({'message': 'User registered successfully!'})
        except Exception as e:
            # Return a meaningful error message as a JSON response
            return JsonResponse({'error': str(e)}, status=400)
    else:
        # Return information about the registration process for GET requests
        return JsonResponse({'message': 'You have successfully reached the registration page.'})