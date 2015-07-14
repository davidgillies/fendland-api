"""
Django app settings for api_renderer and html_renderer.
"""
from .models import Volunteer, Appointment
from .forms import VolunteerForm

# XML_FILE = 'U:/Data/forms_api/forms_api/xmlfiles/Ships.xml'
XML_FILE = 'xmlfiles/Fenland.xml'

DATABASE = 'mysql+pymysql://david:david@localhost:3306/mydb'
# DATABASE = 'sqlite:///U:\\Data\\fenland_api\\db.sqlite3'

DB_MAPPING = {'surgery': 'surgeries_id', 'surgeries': 'surgeries_id', 'diabetes': 'diabetes_diagnosed'}
# DB_MAPPING = {}

# SECTION_MAPPING = {0: 'ships_ship', 1: 'ships_ship', 2: 'ships_ship'}
SECTION_MAPPING = {0: 'volunteers', 1: 'volunteers', 2: 'volunteers',
                    3: 'volunteers', 4: 'volunteers'}
#SECTION_MAPPING = {0: 'famhist_new_famhistquestionnaire', 1: 'famhist_new_famhistquestionnaire', 2: 'famhist_new_famhistquestionnaire',
#                   3: 'famhist_new_famhistquestionnaire', 4: 'famhist_new_famhistquestionnaire'}

TABLE_MODEL_MAPPING = {'volunteers': Volunteer, 'appointments': Appointment}

MODEL_LIST = [Volunteer, Appointment]

MODELS = False

MODEL_MAPPING = {0: Volunteer, 1: Volunteer, 2: Volunteer, 3: Volunteer, 4: Volunteer}

MODEL_FORM_MAPPING = {0: VolunteerForm, 1: VolunteerForm, 2: VolunteerForm,
                      3: VolunteerForm, 4: VolunteerForm}

CUSTOM = True

TESTING = True
