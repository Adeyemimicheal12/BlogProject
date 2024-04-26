from django.shortcuts import render
from .serializers import UserSerializer,UserLoginSerializer
from rest_framework import generics,status
from django.contrib.auth import get_user_model,authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny

User = get_user_model()
# Create your views here.

class UserSignUpApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password'))
            # Save the user object with the hashed password
            user.save()
            return Response({'message': 'User Registration Success'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email_or_username = serializer.validated_data["email_or_username"]
            password = serializer.validated_data["password"]

            user = authenticate(username=email_or_username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                response_data = {'token': token.key,"user_id":user.id }
                return Response(response_data, status=status.HTTP_200_OK)
        
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    