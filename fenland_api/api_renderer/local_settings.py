"""
Django app settings for api_renderer and html_renderer.
"""
from .models import Volunteer

XML_FILE = 'U:/Data/forms_api/forms_api/xmlfiles/Fenland.xml'

DATABASE = 'mysql+pymysql://david:david@localhost:3306/mydb'

DB_MAPPING = {'surgery': 'surgeries_id', 'diabetes': 'diabetes_diagnosed'}

SECTION_MAPPING = {0: 'volunteers', 1: 'volunteers', 2: 'volunteers'}

MODELS = True

MODEL_MAPPING = {0: Volunteer, 1: Volunteer, 2: Volunteer}

CUSTOM = True

TESTING = True
