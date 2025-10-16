from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Expense


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email",  "first_name", "last_name"]

    def create(self, validated_data):
        
        user_obj = User.objects.create_user(**validated_data)
        return user_obj

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id"]

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = "__all__"
        read_only_fields = ["id"]

