"""
Django app settings for api_renderer and html_renderer.
"""

DATABASE = 'mysql+pymysql://david:david@localhost:3306/sm_db'

DB_MAPPING = {'surgery': 'surgery_id', 'diabetes': 'diabetes_diagnosed'}

SECTION_MAPPING = {0: 'volunteers', 1: 'volunteers', 2: 'volunteers'}

MODELS = False

CUSTOM = False
