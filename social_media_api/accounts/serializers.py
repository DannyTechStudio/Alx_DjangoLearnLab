from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

#------- Registration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture']
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    
#------- Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credential")