from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Company
from .models import Team
from .serializers import TeamSerializer, CompanySerializer, EmployeeSerializer

class TeamView(APIView):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, format=None, **kwargs):
        #antes pegar o company id para verificar se o time pertence aquela empresa
        if kwargs.get('company_id'):
            try:
                company = Company.objects.get(id=kwargs['company_id'])
            except ObjectDoesNotExist:
                return Response({"error": "could not find company"}, status=400)
        if kwargs.get('team_id'):
            try:
                #verificar aqui se esse team pertence a company?
                team = Team.objects.get(id=kwargs['team_id'])
                team_data = TeamSerializer(team)
                return Response(team_data.data)
            except ObjectDoesNotExist:
                return Response({"error": "could not find team"}    , status=400)
        else:
            all_teams = Team.objects.all()
            all_teams_serialized = TeamSerializer(all_teams, many=True)
            return Response(all_teams_serialized.data)

    def post(self, request, format=None, **kwargs):
        response = Response()
        new_team = Team(**kwargs)
        new_team.save()

        if new_team:
            response.status_code = 201
        else:
            response.status_code = 400
        return response

class CompanyView(APIView):
    serializer_class = CompanySerializer

    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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