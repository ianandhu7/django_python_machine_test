from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.authtoken.models import Token


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User registered successfully",
                    "data": {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email
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


class UserRetrieveUpdateDeleteView(APIView):

    def get(self, request, **kwargs):
        id = kwargs.get('pk')
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        id = kwargs.get('pk')
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Update failed", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        id = kwargs.get('pk')
        user = User.objects.get(id=id)
        user.delete()
        return Response("Deleted successfully", status=status.HTTP_200_OK)
