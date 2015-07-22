from lxml import objectify
from copy import deepcopy
from itertools import chain
from bunch import Bunch
import datetime
import simplejson
import local_settings
from django.forms.models import model_to_dict
from validator import Validator
from .cam_querysets import QuerySet


def logger(func):
    def inner(*args, **kwargs):
        print "Args: %s, %s" % (args, kwargs)
        return func(*args, **kwargs)
    return inner


class MethodMixin(object):
    def set_rendering_hint(self, item):
        key = item.rhType.text
        self.rendering_hints[key] = ''
        for rhdata in item.rhData:
            self.rendering_hints[key] = self.rendering_hints[key] + ' ' + str(rhdata)
        self.rendering_hints[key] = self.rendering_hints[key].strip()

    def tag_type(self, tag_type):
        return {'{http://www.mrc-epid.cam.ac.uk/schema/common/epi}title': self.set_title, 
                '{http://www.mrc-epid.cam.ac.uk/schema/common/epi}info': self.set_info,
                '{http://www.mrc-epid.cam.ac.uk/schema/common/epi}renderingHint': self.set_rendering_hint,
                '{http://www.mrc-epid.cam.ac.uk/schema/common/epi}externalPrograms': self.set_external_programs,
                '{http://www.mrc-epid.cam.ac.uk/schema/common/epi}option': self.set_options,
                '{http://www.mrc-epid.cam.ac.uk/schema/common/epi}restrictions': self.set_restrictions,
                '{http://www.mrc-epid.cam.ac.uk/schema/common/epi}textNode': self.set_text_node,
                '{http://www.mrc-epid.cam.ac.uk/schema/common/epi}question': self.set_question,
                '{http://www.mrc-epid.cam.ac.uk/schema/common/epi}questionGroup':self.set_question_group,
                '{http://www.mrc-epid.cam.ac.uk/schema/common/epi}variable': self.set_variable,
                '{http://www.mrc-epid.cam.ac.uk/schema/common/epi}rtConditions': self.set_rtConditions,
                }[tag_type]

    def __str__(self):
        return "%s: %s" % (self.title, self.position)

    def __unicode__(self):
        return "%s: %s" % (self.title, self.position)
        
    def set_rtConditions(self, item):
        pass

    def set_title(self, item):
        pass

    def set_variable(self, item):
        pass

    def set_options(self, item):
        pass

    def set_info(self, item):
        pass

    def set_external_programs(self, item):
        pass

    def set_text_node(self, item):
        pass

    def set_question(self, item):
        pass

    def set_question_group(self, item):
        pass

    def set_restrictions(self, item):
        pass


class Question(MethodMixin):
    def __init__(self, question_object, app_object, section_object):
        self.app_object = app_object
        self.question_objects = []
        self.section = section_object
        self.title = question_object.attrib['position']
        self.variable = question_object.variable.varName.text
        self.var_value = None
        self.var_id = None
        self.required = False
        self.dynamic = False
        self.maxlength = 0
        self.multi = False
        self.tests = []
        self.info = []
        self.data_type = {}
        self.pattern = ''
        self.id = question_object.attrib['ID']
        self.position = question_object.attrib['position']
        self.rendering_hints = {}
        self.restrictions = {}
        self.template = ''
        self.template_args = {'options': []}
        self.model = None
        self.build_question(question_object)
        self.validator_rules()
        self.app_object.validator[self.variable] = self

    def set_model(self):
        if self.variable in self.app_object.db_mapping.keys():
            variable = self.app_object.db_mapping[self.variable]
        else:
            variable = self.variable
        if self.app_object.models:
            section_model = self.app_object.model_mapping[int(self.section.position)]

            if variable in section_model._meta.get_all_field_names():
                self.model = section_model
            elif 'multi' in self.rendering_hints.keys():
                if variable in self.app_object.table_model_mapping[self.rendering_hints['multi']]._meta.get_all_field_names():
                    self.app_object.table_model_mapping[self.rendering_hints['multi']]._meta.get_all_field_names()
                    self.model = self.app_object.table_model_mapping[self.rendering_hints['multi']]

    def validator_rules(self):
        rules = {}
        try:
            rules['type'] = self.data_type['type']
            self.tests.append('type')
            try:
                self.pattern = self.data_type['pattern']
            except:
                pass
        except:
            pass
        if 'CheckMaxLength' in self.restrictions.keys():
            rules['CheckMaxLength'] = self.data_type['maxLength']
            self.maxlength = self.data_type['maxLength']
            self.tests.append('CheckMaxLength')
        if 'IsAnswered' in self.restrictions.keys():
            if self.restrictions['IsAnswered']['AllowError'] == 'false':
                rules['IsAnswered'] = True
                self.required = True
                self.tests.append('IsAnswered')
        return rules

    def get_template(self, selection):
        return {'radio': 'html_renderer/radio.html',
                'dropdown': 'html_renderer/select.html',
                'text': 'html_renderer/text.html',
                'multiline': 'html_renderer/textarea.html',
                'range': 'html_renderer/range.html',
                'datalist': 'html_renderer/datalist.html',
                'search': 'html_renderer/search.html',
                'altradio': 'html_renderer/alt_radio.html',
                'altdropdown': 'html_renderer/alt_select.html',
                'alttext': 'html_renderer/alt_text.html',
                'altmultiline': 'html_renderer/alt_textarea.html',
                'altrange': 'html_renderer/alt_range.html',
                'altdatalist': 'html_renderer/alt_datalist.html',
                'altsearch': 'html_renderer/alt_search.html'}[selection]

    def set_template(self):
        if local_settings.QUESTIONNAIRE:
            qtype = 'alt' + self.rendering_hints['qtype']
            self.template = self.get_template(qtype)
        else:
            self.template = self.get_template(self.rendering_hints['qtype'])

    def build_question(self, question_object):
        for item in question_object.getchildren():
            self.tag_type(item.tag)(item)
        self.set_template()
        self.set_model()

    def set_options(self, item):
        try:
            if item.optionText.text == 'dynamic':
                self.template_args['options'] = self.get_options(item.optionValue.text)
                self.dynamic = True
            else:
                self.template_args['options'].append({'text': item.optionText.text, 'value': item.optionValue.text})
        except:
            self.template_args['options'].append({'text': item.optionValue.text, 'value': item.optionValue.text})

    def get_options(self, item):
        pass

    def set_info(self, item):
        q_info = {}
        q_info['text'] = item.text
        q_info['cssClass'] = item.attrib['cssClass']
        try:
            q_info['cssClass'] = item.attrib['cssClass']
        except:
            q_info['cssClass'] = ''
        self.info.append(q_info)

    def set_restrictions(self, item):
        for rule in item.getchildren():
            parameters = {}
            for p in rule.getchildren():
                parameters[p.attrib['use']] = p.text
            self.restrictions[rule.attrib['name']] = parameters

    def set_variable(self, item):
        """Sets the variable data type.  Variable name has already been set."""
        try:
            for dt in item.dataType.getchildren():
                self.data_type['type'] = dt.tag.replace('{http://www.mrc-epid.cam.ac.uk/schema/common/epi}', '')
                for child in dt.getchildren():
                    self.data_type[child.tag.replace('{http://www.mrc-epid.cam.ac.uk/schema/common/epi}', '')] = child.text
        except:
            pass

# Tod dos:
# 1. set table and shownumber on the QuestionGroup object, they come from
# the renderingHints.
# 2. Is there anything that can be rendered entirely by a template to string
# that doesn't have any data...  First sections etc.  Does it help?


class QuestionGroup(MethodMixin):
    def __init__(self, question_group_object, app_object, section_object):
        self.app_object = app_object
        self.section = section_object
        self.question_group_objects = []
        self.info = []
        self.title = question_group_object.title
        self.position = question_group_object.attrib['position']
        self.rendering_hints = {}
        self.build_question_group(question_group_object)

    def build_question_group(self, question_group_object):
        for item in question_group_object.getchildren():
            self.tag_type(item.tag)(item)

    def set_info(self, item):
        qg_info = {}
        qg_info['text'] = item.text
        try:
            qg_info['cssClass'] = item.attrib['cssClass']
        except:
            qg_info['cssClass'] = ''
        self.info.append(qg_info)

    def set_text_node(self, item):
        text_node = Bunch()
        text_node.rendering_hints = {}
        try:
            text_node['id'] = item.attrib['ID']
        except:
            text_node['id'] = None
        text_node['position'] = item.attrib['position']
        try:
            text_node['text'] = item.info.text
        except:
            text_node['text'] = ''
        try:
            for rh in item.renderingHint:
                key = rh.rhType.text
                text_node.rendering_hints[key] = ''
                for rhdata in rh.rhData:
                    text_node.rendering_hints[key] = text_node.rendering_hints[key] + ' ' + str(rhdata)
                text_node.rendering_hints[key] = text_node.rendering_hints[key].strip()
        except:
            pass
        self.question_group_objects.append(text_node)

    # @logger
    def set_question(self, item):
        question = Question(item, self.app_object, self.section)
        self.question_group_objects.append(question)

    def get_question(self, question):
        for q in self.question_group_objects:
            if q.position == question:
                return q


class Section(MethodMixin):
    def __init__(self, section_xml_object, app_object):
        """Initializes Section object."""
        self.app_object = app_object  # reference to parent
        self.section_xml_object = section_xml_object  # section xml
        self.title = section_xml_object.title
        self.position = section_xml_object.attrib['position']
        self.testing = local_settings.TESTING
        self.info = []
        self.api = {}
        self.question_groups = []
        self.errors = {}
        self.section_objects = []
        self.rendering_hints = {}
        self.build_section()

    def build_section(self):
        """sets Question Group instance's properties."""
        for item in self.section_xml_object.getchildren():
            self.tag_type(item.tag)(item)

    def set_info(self, item):
        """Sets properties with Info tag."""
        section_info = {}
        section_info['text'] = item.text
        try:
            section_info['cssClass'] = item.attrib['cssClass']
        except:
            section_info['cssClass'] = ''
        self.info.append(section_info)
        # self.section_objects.append(section_info)

    def set_question_group(self, item):
        """Creates Question Group instances."""
        question_group = QuestionGroup(item, self.app_object, self)
        self.question_groups.append(question_group)
        self.section_objects.append(question_group)

    def get_question_group(self, question_group):
        for qg in self.question_groups:
            if qg.position == question_group:
                return qg

    def section_to_dict(self):
        """Converts Section instance copy to dictionary."""
        data = {}
        multi = False
        for qg in self.section_objects:
            data_dict = {}
            for q in qg.question_group_objects:
                if isinstance(q, Question):
                    if 'multi' in q.rendering_hints.keys() or multi is True:
                        if multi is False:
                            multi = True
                            multi_name = q.rendering_hints['multi']
                            if multi_name not in data.keys():
                                data[multi_name] = []
                        data_dict['id'] = q.var_id
                        if isinstance(q.var_value, datetime.timedelta):
                            data_dict[q.variable[:-2]] = str(q.var_value)
                        else:
                            data_dict[q.variable[:-2]] = q.var_value
                        if 'endoftr' in q.rendering_hints.keys():
                            multi = False
                            data[multi_name].append(data_dict)
                            data_dict = {}
                    else:
                        if isinstance(q.var_value, datetime.timedelta):
                            data[q.variable] = str(q.var_value)
                        else:
                            data[q.variable] = q.var_value
        return data


class Application(object):
    def __init__(self, name, xml):
        """Initializes the Application object."""
        self.name = name
        self.xml = xml
        self.validator = {}
        self.xml_object = objectify.fromstring(self.xml)
        self.id = self.xml_object.attrib['ID']
        self.models = local_settings.MODELS
        self.custom = local_settings.CUSTOM
        self.mapping = local_settings.SECTION_MAPPING
        self.db_mapping = local_settings.DB_MAPPING
        self.model_mapping = local_settings.MODEL_MAPPING
        self.model_form_mapping = local_settings.MODEL_FORM_MAPPING
        self.table_model_mapping = local_settings.TABLE_MODEL_MAPPING
        self.testing = local_settings.TESTING
        self.author = self.xml_object.author
        self.version_number = self.xml_object.versionNumber
        self.version_date = self.xml_object.versionDate
        self.title = self.xml_object.title
        self.studyname = self.xml_object.studyName
        self.sections = self.get_sections()

    # @logger
    def get_data(self, section_number, id_variable, id_variable_value):
        """Returns section data."""
        if self.models:
            data = model_to_dict(self.model_mapping[int(section_number)].objects.get(id=id_variable_value))
        else:
            queryset = QuerySet(table_name=self.get_table_name(section_number),
                                id_variable_value=id_variable_value)
            data = queryset.get()
        return data

    def tidy(self, data):
        for k in data.keys():
            if isinstance(data[k], datetime.date):
                data[k] = str(data[k])

    def insert_data(self, section_number, id_variable, body):
        json_dict = simplejson.JSONDecoder().decode(body)
        if self.models:
            json_dict = self.pre_process_keys(json_dict)
            validator = self.model_form_mapping[int(section_number)](json_dict)
            if validator.is_valid():
                json_dict = self.post_process_keys(json_dict)
                model = self.model_mapping[int(section_number)].objects.create(**json_dict)
                data = model_to_dict(model)
            else:
                errors = {}
                for field in validator:
                    errors[field.label] = field.errors
                data = json_dict
                data['errors'] = 'errors'
        else:
            if 'search' in json_dict.keys():
                data = self.search(json_dict['search'], section_number)
            else:
                validator = Validator(self.validator, json_dict)
                print json_dict, self.validator
                if validator.is_valid():
                    for k in json_dict.keys():
                        if k in self.db_mapping.keys():
                            json_dict[self.db_mapping[k]] = json_dict[k]
                            json_dict.pop(k)
                    queryset = QuerySet(table_name=self.get_table_name(section_number))
                    data = queryset.create(json_dict)
                else:
                    for k in json_dict.keys():
                        if k in self.db_mapping.keys():
                            json_dict[self.db_mapping[k]] = json_dict[k]
                            json_dict.pop(k)
                    data = json_dict
                    data['errors'] = validator.errors
        return data

    def pre_process_keys(self, json_dict):
        pass

    def post_process_keys(self, json_dict):
        pass

    def update_data(self, section_number, id_variable, id_variable_value,
                    body):
        if self.models:
            json_dict = simplejson.JSONDecoder().decode(body)
            orig_json_dict = json_dict
            json_dict = self.pre_process_keys(json_dict)
            for k in json_dict.keys():
                if k in self.db_mapping.keys():
                    json_dict[self.db_mapping[k]] = json_dict[k]
                    json_dict.pop(k)
            validator_form = self.model_form_mapping[int(section_number)](json_dict)
            if validator_form.is_valid():
                self.model_mapping[int(section_number)].objects.filter(pk=id_variable_value).update(**json_dict)
                data = model_to_dict(self.model_mapping[int(section_number)].objects.get(id=id_variable_value))
            else:
                errors = {}
                for field in validator_form:
                    errors[field.label] = field.errors.as_text()
                data = orig_json_dict
                data['errors'] = errors
        else:
            json_dict = simplejson.JSONDecoder().decode(body)
            validator = Validator(self.validator, json_dict)
            if validator.is_valid():
                for k in json_dict.keys():
                    if k in self.db_mapping.keys():
                        json_dict[self.db_mapping[k]] = json_dict[k]
                        json_dict.pop(k)
                queryset = QuerySet(table_name=self.get_table_name(section_number))
                queryset.update(json_dict, id_variable_value)
                data = queryset.data
            else:
                for k in json_dict.keys():
                    if k in self.db_mapping.keys():
                        json_dict[self.db_mapping[k]] = json_dict[k]
                        json_dict.pop(k)
                data = json_dict
                data['errors'] = validator.errors
        return data

    def delete_data(self, section_number, id_variable, id_variable_value):
        if self.models:
            self.model_mapping[int(section)].objects.get(id=id_variable_value).delete()
        else:
            queryset = QuerySet(table_name=self.get_table_name(section_number),
                                id_variable_value=id_variable_value)
            queryset.delete()
        return

    def get_table_name(self, section_number):
        return self.mapping[int(section_number)]

    def get_section(self, section_number):
        return deepcopy(self.sections[str(section_number)])

    def get_sections(self):
        """Instantiates Section objects for each section."""
        sections = {}
        for section in self.xml_object.section:
            sections[section.attrib['position']] = Section(section, self)
        return sections

    def search(self, search_term, section_number):
        """Filler function should be overwritten in subclass."""
        pass


class DataPrep(object):
    def __init__(self, section, data):
        self.data = data
        self.section = section
        self.Question = Question

    def data_prep(self):
        if 'errors' in self.data.keys():
            self.section.errors = self.data['errors']
#        for qg in self.section.section_objects:
#            for q in qg.question_group_objects:
#                print q
#                print type(q)
#                if isinstance(q, self.Question):
#                    print q.rendering_hints
        try:
            for qg in self.section.section_objects:
                multi_lines = []
                multi = False
                multi_line = []
                for q in qg.question_group_objects:
                    if 'multi' in q.rendering_hints.keys() or multi:
                        if multi is False:
                            multi_index = qg.question_group_objects.index(q)
                        multi_line.append(q)
                        multi = True
                        if 'endoftr' in q.rendering_hints.keys():
                            multi = False
                            multi_data = self.get_multi_data(multi_line[0].rendering_hints['multi'], self.data['id'])
                            multi_line_adder = []
                            for i in range(len(multi_data)):
                                multi_line_adder.append(deepcopy(multi_line))
                            multi_line = multi_line_adder
                            for index in range(len(multi_line)):
                                for i in range(len(multi_line[index])):
                                    if isinstance(multi_line[index][i], self.Question):
                                        try:
                                            multi_line[index][i].var_value = multi_data[index][multi_line[index][i].variable]
                                            multi_line[index][i].multi = True
                                        except:
                                            multi_line[index][i].required = False
                                        try:
                                            multi_line[index][i].var_id = multi_data[index]['id']
                                        except:
                                            pass
                                        multi_line[index][i].variable = 'multi_' + multi_line[index][i].variable + '_' + str(index)
                            multi_line = list(chain.from_iterable(multi_line))
                            multi_lines.append([multi_line, multi_index])
                    elif isinstance(q, self.Question):
                        self.add_question_value(q)
                for ml in multi_lines:
                    qg.question_group_objects[ml[1]:ml[1]+(len(ml[0])/len(multi_data))] = ml[0]
            return self.section
        except:
           return self.section

    def get_multi_data(self, table, id):
        pass

    def add_question_value(self, q):
        q.var_value = self.data[q.variable]
