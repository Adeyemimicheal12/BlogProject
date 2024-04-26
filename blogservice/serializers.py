from rest_framework import serializers
from .models import Category,BlogPost
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()

catergory_unique_validator = UniqueValidator(queryset=Category.objects.all(),lookup="iexact",message="This catergory already exists.")
class CaterorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[catergory_unique_validator])
    class Meta:
        model = Category
        fields = "__all__"

class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    full_name = serializers.CharField(read_only=True,source='get_full_name')

class BlogPostSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(read_only=True)
    class Meta:
        model = BlogPost
        fields = "__all__"
        read_only_fields = ['author']
        