from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    full_name = serializers.CharField(source='get_full_name',read_only=True)

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password','full_name','bio','date_joined']
        read_only_fields = ['bio','date_joined']
        
    def validate_email(self, value):
        # Normalize the email address
        normalized_email = value.lower().strip()
        if User.objects.filter(email=normalized_email).exists():
            raise serializers.ValidationError("This email address is already in use.")
        return normalized_email
    
    def validate_username(self, value):
        # Normalize the username field
        normalized_username = value.lower().strip()
        if User.objects.filter(username=normalized_username).exists():
            raise serializers.ValidationError("This username address is already in use.")
        return normalized_username

   
class UserLoginSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    password = serializers.CharField(style={"input":"password"})
    
    def validate_email_or_username(self,value):
        value = value.lower().strip()
        return value