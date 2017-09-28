from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
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
            return Response(None)

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