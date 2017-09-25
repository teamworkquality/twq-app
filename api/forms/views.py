from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Form

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