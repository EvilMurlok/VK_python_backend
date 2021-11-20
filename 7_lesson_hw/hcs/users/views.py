from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.response import Response

from .serializers import DetailUsersSerializer
from .serializers import CreateUserSerializer
from .serializers import UpdateUserUserInfoSerializer
from .serializers import UpdateUserUsernameSerializer
from .models import Users


# для просмотра можно использовать такую простенькую вьюху
class UsersListView(generics.ListAPIView):
    serializer_class = DetailUsersSerializer
    queryset = Users.objects.all()


# тут под капотом post-запрос
class UsersCreateView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer


class UsersDeleteView(generics.DestroyAPIView):
    serializer_class = DetailUsersSerializer
    queryset = Users.objects.all()

    def get(self, request, pk):
        required_user = get_object_or_404(Users, pk=pk)
        serializer = DetailUsersSerializer(required_user)
        return Response(serializer.data)


class UsersUpdateUserInfoView(generics.UpdateAPIView):
    serializer_class = UpdateUserUserInfoSerializer
    queryset = Users.objects.all()

    def get(self, request, pk):
        required_user = get_object_or_404(Users, pk=pk)
        serializer = DetailUsersSerializer(required_user)
        return Response(serializer.data)


class UserUpdateUsernameView(generics.UpdateAPIView):
    serializer_class = UpdateUserUsernameSerializer
    queryset = Users.objects.all()

    def get(self, request, pk):
        required_user = get_object_or_404(Users, pk=pk)
        serializer = DetailUsersSerializer(required_user)
        return Response(serializer.data)
