from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseNotFound
from custom_logic import CustomApplication
from .models import *


xml_string = open('U:/Data/forms_api/forms_api/xmlfiles/Fenland.xml', 'r').read()
fenland_app = CustomApplication('fenland', xml_string)


class APIView(APIView):
    def get(self, request, section=None, id_variable=None,
            id_variable_value=None):
        if id_variable is None or id_variable_value is None:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        else:
            data = fenland_app.get_data(section, id_variable, id_variable_value)
            response = Response(data, status=status.HTTP_200_OK)
            return response
            
    def post(self, request, section=None, id_variable=None,
             id_variable_value=None):
        data = fenland_app.insert_data(section, id_variable, id_variable_value, request.body)
        response = Response(data, status=status.HTTP_201_CREATED)
        return response

    def put(self, request, section=None, id_variable=None,
            id_variable_value=None):
        data = fenland_app.update_data(section, id_variable, id_variable_value, request.body)
        response = Response(data, status=status.HTTP_200_OK)
        return response

    def delete(self, request, section=None, id_variable=None,
               id_variable_value=None):
        fenland_app.delete_data(section, id_variable, id_variable_value)
        return Response(status=status.HTTP_204_NO_CONTENT)
