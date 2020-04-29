from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Profile


class CustomRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(
            validated_data['name'],
            validated_data['email'],
            validated_data['password']
        )
        user.username = validated_data['name']
        return user
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
            'name': self.validated_data.get('username', ''),
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'name', 'image', 'bio')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
