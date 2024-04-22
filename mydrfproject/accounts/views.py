from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Return a customized success response with user_id
            return Response({'message': 'User registered successfully', 'user_id': user.id}, status=status.HTTP_201_CREATED)
        # Customize error handling to provide informative messages
        errors = serializer.errors
        if 'email' in errors:
            message = 'Invalid email format'
        elif 'password' in errors:
            message = 'Password must be at least 8 characters long'
        else:
            message = 'Failed to register user'
        return Response({'message': message, 'errors': errors}, status=status.HTTP_400_BAD_REQUEST)
