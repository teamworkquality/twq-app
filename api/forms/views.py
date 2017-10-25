from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Form
from .serializers import FormSerializer

class FormsView(APIView):

    queryset = Form.objects.all()

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
        print(request.data)
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
            form = Form.objects.get(id = kwargs['form_id'])
            if form:
                serializer = FormSerializer(form, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

