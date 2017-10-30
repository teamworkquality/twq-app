from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from companies.models import Company, Team
from users.models import User, Employee
from users.serializers import UserSerializer, EmployeeSerializer


class UserView(APIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, format=None, **kwargs):
        if kwargs.get('user_id'):
            try:
                user = User.objects.get(id=kwargs['user_id'])
                user_data = UserSerializer(user)
                return Response(user_data.data)
            except ObjectDoesNotExist:
                return Response({"error": "could not find user"}    , status=400)
        else:
            all_users = User.objects.all()
            all_users_serialized = UserSerializer(all_users, many=True)
            return Response(all_users_serialized.data)

    def post(self, request, format=None, **kwargs):
        response = Response()
        new_user = User(**kwargs)
        new_user.save()

        if new_user:
            response.status_code = 201
        else:
            response.status_code = 400
        return response

    def delete(self, request, format=None, **kwargs):
        response = Response()
        if kwargs.get("user_id"):
            user = User.objects.get(id=kwargs['user_id'])
            if user:
                user.delete()
                response.status_code = 204
            else:
                pass
        else:
            response.status_code = 400

        return response

class EmployeeView(APIView):
    serializer_class = EmployeeSerializer
    def get(self, request, format=None, **kwargs):
        if kwargs.get('company_id'):
            try:
                company = Company.objects.get(id=kwargs.get('company_id'))
            except Company.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        if kwargs.get('team_id'):
            try:
                team = Team.objects.get(id=kwargs.get('company_id'))
            except Team.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        employees = Employee.objects.filter(employer=company, team=team)

        serializer = Employee(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)