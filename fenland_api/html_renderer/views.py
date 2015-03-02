from django.views.generic import View
from cam_apps import Application

xml_string = open('U:/Data/forms_api/forms_api/xmlfiles/Fenland.xml', 'r').read()
fenland_app = Application('fenland', xml_string)

class HTMLView(View):
    pass
