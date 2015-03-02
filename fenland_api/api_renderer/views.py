from django.views.generic import View
from django.http import HttpResponse, HttpResponseNotFound
from cam_apps import Application


xml_string = open('U:/Data/forms_api/forms_api/xmlfiles/Fenland.xml', 'r').read()
fenland_app = Application('fenland', xml_string)

class APIView(View):
    def get(self, request, section=None, id_variable=None,
            id_variable_value=None):
        if id_variable is None or id_variable_value is None:
            return HttpResponseNotFound('<h1>Page not found</h1>')
        else:
            data = apps_xml.apps[xml].get_data(section, id_variable, id_variable_value)
            return HttpResponse(json.dumps(data), content_type='application/json; charset=UTF-8')

    def post(self, request, section=None, id_variable=None,
             id_variable_value=None):
        data = apps_xml.apps[xml].insert_data(section, id_variable, id_variable_value, request.body)
        return HttpResponse(json.dumps(data), content_type='application/json; charset=UTF-8', status=201)

    def put(self, request, section=None, id_variable=None,
            id_variable_value=None):
        data = apps_xml.apps[xml].update_data(section, id_variable, id_variable_value, request.body)
        return HttpResponse(json.dumps(data), content_type='application/json; charset=UTF-8')

    def delete(self, request, section=None, id_variable=None,
               id_variable_value=None):
        data = apps_xml.apps[xml].delete_data(section, id_variable, id_variable_value)
        return HttpResponse(None, status=204)
