from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer


class UserView(APIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None, **kwargs):
        if kwargs.get('user_id'):
            print("id received")
        else:
            print("list users")
        return Response()

    def post(self, request, user_id, format=None):
        return Response()

    def delete(self, request, user_id, format=None):
        return Response()