from django.shortcuts import get_object_or_404

from rest_framework import generics, status, permissions
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from .serializers import DetailUsersSerializer, ChangePasswordSerializer
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


class UsersRetrieveDeleteView(generics.RetrieveDestroyAPIView):
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


class UserUpdatePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    queryset = Users.objects.all()
    model = Users
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
