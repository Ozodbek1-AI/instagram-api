from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.accounts.models import User


class CreateUserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','password','full_name','username','created_at']
        read_only_fields = ['id','created_at','updated_at']
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate_username(self,value):
        if len(value) < 0:
            raise serializers.ValidationError("Username must not be empty.")
        return value

    def validate_email(self,value:str):
        if value.endswith("@gmail.com"):
            raise serializers.ValidationError("Email must end with @gmail.com")
        return value

    def validate_password(self,value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be longer than 8 characters.")
        return value

    def validate_first_name(self,value:str):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("First name should not contain a number.")
        return value

    def validate_last_name(self,value:str):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Last name should not contain a number.")
        return value

    def validate_phone(self,value:str):
        if len(value) < 12:
            raise serializers.ValidationError("Phone number must be 13 digits long")
        if not value.startswith("+998"):
            raise serializers.ValidationError("Phone number start with '+998'")
        return value



class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self, attrs):
        credentials = {
            'username': attrs.get('username'),
            'password': attrs.get('password')
        }
        user = authenticate(request=self.context['request'], **credentials)
        if user is None:
            raise serializers.ValidationError('Username or password is incorrect')
        else:
            attrs['user'] = user
            return attrs


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','full_name','username','created_at']
        read_only_fields = ['id','created_at']


    def validate_username(self,value):
        if len(value) < 0:
            raise serializers.ValidationError("Username must not be empty.")
        return value

    def validate_email(self,value:str):
        if value.endswith("@gmail.com"):
            raise serializers.ValidationError("Email must end with @gmail.com")
        return value

    def validate_password(self,value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be longer than 8 characters.")
        return value

    def validate_first_name(self,value:str):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("First name should not contain a number.")
        return value

    def validate_last_name(self,value:str):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Last name should not contain a number.")
        return value

    def validate_phone(self,value:str):
        if len(value) < 12:
            raise serializers.ValidationError("Phone number must be 13 digits long")
        if not value.startswith("+998"):
            raise serializers.ValidationError("Phone number start with '+998'")
        return value