"""
Django app settings for api_renderer and html_renderer.
"""
from .models import Volunteer
from .forms import VolunteerForm

#XML_FILE = 'U:/Data/forms_api/forms_api/xmlfiles/Ships.xml'
XML_FILE = 'U:/Data/forms_api/forms_api/xmlfiles/Fenland.xml'

DATABASE = 'mysql+pymysql://david:david@localhost:3306/mydb'
#DATABASE = 'sqlite:///U:\\Data\\fenland_api\\db.sqlite3'

DB_MAPPING = {'surgery': 'surgeries_id', 'surgeries': 'surgeries_id', 'diabetes': 'diabetes_diagnosed'}
#DB_MAPPING = {}

#SECTION_MAPPING = {0: 'ships_ship', 1: 'ships_ship', 2: 'ships_ship'}
SECTION_MAPPING = {0: 'volunteers', 1: 'volunteers', 2: 'volunteers'}

MODELS = False

MODEL_MAPPING = {0: Volunteer, 1: Volunteer, 2: Volunteer}

MODEL_FORM_MAPPING = {0: VolunteerForm, 1: VolunteerForm, 2: VolunteerForm}

CUSTOM = True

TESTING = True
