from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import Admin
from users.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework import status


class UserView(APIView):

    queryset = Admin.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None, **kwargs):
        if kwargs.get('user_id'):
            try:
                user = Admin.objects.get(id=kwargs['user_id'])
                user_data = UserSerializer(user)
                return Response(user_data.data)
            except ObjectDoesNotExist:
                return Response({"error": "could not find user"}, status=400)
        else:
            all_users = Admin.objects.all()
            all_users_serialized = UserSerializer(all_users, many=True)
            return Response(all_users_serialized.data)

    def post(self, request, format=None):
        response = Response()
        #hashs password for proper safety
        user_data = request.data.copy()
        user_data["password"] = make_password(user_data["password"])

        new_user = UserSerializer(data=user_data)

        if new_user.is_valid():
            user = new_user.save()
            response.status_code = 201
            token = Token.objects.create(user=user)
            response['token'] = token.key
        else:
            response.status_code = 400
            response['error'] = new_user.errors
        return response

    def delete(self, request, format=None, **kwargs):
        response = Response()
        if kwargs.get("user_id"):
            user = Admin.objects.get(id=kwargs['user_id'])
            if user:
                user.delete()
                response.status_code = 204
            else:
                pass
        else:
            response.status_code = 400

        return response


class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                token = Token.objects.get(user=user).key
                return Response(status=status.HTTP_200_OK, data={"token": token})
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
