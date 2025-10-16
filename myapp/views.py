from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from .serializers import RegisterSerializer, UserSerializer
from .models import Category, Expense


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            return Response(
                {
                    "message": "User registered successfully",
                    "data": {
                        "id": data.id,
                        "username": data.username,
                        "email": data.email
                    }
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"message": "Registration failed", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class UserListCreateView(APIView):
    def get(self, request):
        data = User.objects.all()
        serializer = UserSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "Creation failed"}, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveUpdateDeleteView(APIView):

    def get(self, request, **kwargs):
        id = kwargs.get('pk')
        data = get_object_or_404(User, id=id)
        serializer = UserSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, **kwargs):
        id = kwargs.get('pk')
        existing = get_object_or_404(User, id=id)
        serializer = UserSerializer(existing, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"message": "Update failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




    def delete(self, request, **kwargs):
        id = kwargs.get('pk')
        data = get_object_or_404(User, id=id)
        data.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)


class ExpenseSummaryView(APIView):
    def get(self, request, **kwargs):
        category_id = kwargs.get('pk')
        category = get_object_or_404(Category, id=category_id)
        total = Expense.objects.filter(category=category).aggregate(
            total_amount=Sum('amount')
        )['total_amount'] or 0
        return Response({category.name: float(total)})
