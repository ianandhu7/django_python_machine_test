from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Expense

# Simple User registration serializer
class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name"]

    def create(self, validated_data):
        # use create_user to hash password
        user_obj = User.objects.create_user(**validated_data)
        return user_obj

# Simple user listing serializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]

# Category serializer
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id"]

# Expense serializer
class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = "__all__"
        read_only_fields = ["id"]

