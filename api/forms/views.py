from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Form
from analise.analysisCaller import createReport
import numpy as np
from .serializers import FormSerializer, AnswerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class FormsView(APIView):

    queryset = Form.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None, **kwargs):
        if kwargs.get('form_id'):
            try:
                return Response(None)
            except ObjectDoesNotExist:
                return Response({"error": "could not find user"}    , status=400)
        else:
            forms = Form.objects.all()
            forms_serialized = FormSerializer(forms, many=True)
            return Response(forms_serialized.data)

    def post(self, request, format=None, **kwargs):
        response = Response()
        serializer = FormSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response.status_code = 201
            response.data = serializer.validated_data
        else:
            response.status_code = 400
        return response

    def delete(self, request, format=None, **kwargs):
        response = Response()
        if kwargs.get("form_id"):
            form = Form.objects.get(id=kwargs['form_id'])
            if form:
                form.delete()
                response.status_code = 204
            else:
                pass
        else:
            response.status_code = 400

        return response

    def update(self, request, format=None, **kwargs):
        response = Response()
        if kwargs.get("form_id"):
            form = Form.objects.get(id=kwargs['form_id'])
            if form:
                serializer = FormSerializer(form, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswersView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None, **kwargs):
        serializer = AnswerSerializer(request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None, **kwargs):
        self.ci = np.array([[0, 1, "c1"], [2, 4, "c2"]])

        self.data2 = np.array([
            [1, 9, 2, 5, 8, 7],
            [2, 6, 1, 3, 2, 8],
            [3, 8, 4, 6, 8, 3],
            [4, 7, 1, 2, 6, 2],
            [5, 10, 5, 6, 9, 1],
            [6, 6, 2, 4, 7, 0]
        ])
        resultado_obtido = createReport(0, self.data2, self.ci)
        return Response(data=resultado_obtido)

