from lxml import objectify
import sqlsoup
import simplejson
import local_settings
import datetime
from .models import *
from django.forms.models import model_to_dict
from copy import deepcopy
from .forms import VolunteerForm
import arrow
from validator import Validator
from .cam_querysets import QuerySet
from itertools import chain


db = sqlsoup.SQLSoup(local_settings.DATABASE)


def logger(func):
    def inner(*args, **kwargs):
        print "Args: %s, %s" % (args, kwargs)
        return func(*args, **kwargs)
    return inner


class TextNode(dict):
    def __init__(self, position):
        self.rendering_hints = {}
        self.position = position
        super(TextNode, self).__init__()


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
                '{http://www.mrc-epid.cam.ac.uk/schema/common/epi}variable': self.set_variable
                }[tag_type]

    def __str__(self):
        return "%s: %s" % (self.title, self.position)

    def __unicode__(self):
        return "%s: %s" % (self.title, self.position)

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
    def __init__(self, question_object, app_object):
        self.app_object = app_object
        self.question_objects = []
        self.title = question_object.attrib['position']
        self.variable = question_object.variable.varName.text
        self.var_value = None
        self.var_id = None
        self.data_type = {}
        self.id = question_object.attrib['ID']
        self.position = question_object.attrib['position']
        self.rendering_hints = {}
        self.restrictions = {}
        self.template = ''
        self.template_args = {'options': []}
        self.build_question(question_object) 
        self.app_object.validator[self.variable] = self.validator_rules()
        
    def validator_rules(self):
        rules = {}
        if 'CheckMaxLength' in self.restrictions.keys():
            rules['CheckMaxLength'] = self.data_type['maxLength']
        if 'IsAnswered' in self.restrictions.keys():
            if self.restrictions['IsAnswered']['AllowError'] == 'false':
                rules['IsAnswered'] = True
        return rules

    def get_template(self, selection):
        return {'radio': 'html_renderer/radio.html',
                'dropdown': 'html_renderer/select.html',
                'text': 'html_renderer/text.html',
                'multiline': 'html_renderer/textarea.html',
                'range': 'html_renderer/range.html',
                'datalist': 'html_renderer/datalist.html'}[selection]

    def set_template(self):
        self.template = self.get_template(self.rendering_hints['qtype'])

    def build_question(self, question_object):
        for item in question_object.getchildren():
            self.tag_type(item.tag)(item)
        self.set_template()

    def set_options(self, item):
        if item.optionText.text == 'dynamic':
            self.template_args['options'] = self.get_options(item.optionValue.text)
        else:
            self.template_args['options'].append({'text': item.optionText.text, 'value': item.optionValue.text})
            
    def get_options(self, item):
        pass

    def set_info(self, item):
        q_info = {}
        q_info['text'] = item.text
        q_info['cssClass'] = item.attrib['cssClass']
        self.question_objects.append(q_info)

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
    def __init__(self, question_group_object, app_object):
        self.app_object = app_object
        self.question_group_objects = []
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
        qg_info['cssClass'] = item.attrib['cssClass']
        self.question_group_objects.append(qg_info)

    def set_text_node(self, item):
        text_node = TextNode(item.attrib['position'])
        try:
            text_node['id'] = item.attrib['ID']
        except:
            text_node['id'] = None
        text_node['position'] = item.attrib['position']
        text_node['text'] = item.info.text
        for rh in item.renderingHint:
            key = rh.rhType.text
            text_node.rendering_hints[key] = ''
            for rhdata in rh.rhData:
                text_node.rendering_hints[key] = text_node.rendering_hints[key] + ' ' + str(rhdata)
            text_node.rendering_hints[key] = text_node.rendering_hints[key].strip()
        self.question_group_objects.append(text_node)

    def set_question(self, item):
        question = Question(item, self.app_object)
        self.question_group_objects.append(question)

    def get_question(self, question):
        for q in self.question_group_objects:
            if q.position == question:
                return q


class Section(MethodMixin):
    def __init__(self, section_xml_object, app_object):
        self.app_object = app_object
        self.section_xml_object = section_xml_object
        self.title = section_xml_object.title
        self.position = section_xml_object.attrib['position']
        self.testing = local_settings.TESTING
        self.info = []
        self.question_groups = []
        self.errors = {}
        self.section_objects = []
        self.rendering_hints = {}
        self.build_section()

    def build_section(self):
        for item in self.section_xml_object.getchildren():
            self.tag_type(item.tag)(item)

    def set_info(self, item):
        section_info = {}
        section_info['text'] = item.text
        try:
            section_info['cssClass'] = item.attrib['cssClass']
        except:
            section_info['cssClass'] = ''
        self.info.append(section_info)
        self.section_objects.append(section_info)

    def set_question_group(self, item):
        question_group = QuestionGroup(item, self.app_object)
        self.question_groups.append(question_group)
        self.section_objects.append(question_group)

    def get_question_group(self, question_group):
        for qg in self.question_groups:
            if qg.position == question_group:
                return qg


class Application(object):
    def __init__(self, name, xml):
        self.name = name
        self.xml = xml
        self.validator = {}
        self.xml_object = objectify.fromstring(self.xml)
        self.models = local_settings.MODELS
        self.custom = local_settings.CUSTOM
        self.mapping = local_settings.SECTION_MAPPING
        self.db_mapping = local_settings.DB_MAPPING
        self.model_mapping = local_settings.MODEL_MAPPING
        self.testing = local_settings.TESTING
        self.author = self.xml_object.author
        self.version_number = self.xml_object.versionNumber
        self.version_date = self.xml_object.versionDate
        self.title = self.xml_object.title
        self.studyname = self.xml_object.studyName
        self.sections = self.get_sections()

    @logger
    def get_data(self, section_number, id_variable, id_variable_value):
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
        if self.models:
            json_dict = simplejson.JSONDecoder().decode(body)
            if 'dob' in json_dict.keys():
                dob = arrow.get(json_dict['dob'], 'MMMM D, YYYY')
                json_dict['dob'] = dob.format('YYYY-MM-DD')
            validator_form = VolunteerForm(json_dict)
            if validator_form.is_valid():
                if 'surgeries' in json_dict.keys():
                    json_dict['surgeries'] = Surgery.objects.get(id=int(json_dict['surgeries']))
                model = self.model_mapping[int(section_number)].objects.create(**json_dict)
                data = model_to_dict(model)
            else:
                errors = {}
                for field in validator_form:
                    errors[field.label] = field.errors
                data = json_dict
                data['errors'] = 'errors'
        else:
            json_dict = simplejson.JSONDecoder().decode(body)
            for k in json_dict.keys():
                    if k in self.db_mapping.keys():
                        json_dict[self.db_mapping[k]] = json_dict[k]
                        json_dict.pop(k)
            validator = Validator(self.validator, json_dict)
            if validator.is_valid():
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

    def update_data(self, section_number, id_variable, id_variable_value,
                    body):
        if self.models:
            json_dict = simplejson.JSONDecoder().decode(body)
            dob = arrow.get(json_dict['dob'], 'MMMM D, YYYY')
            json_dict['dob'] = dob.format('YYYY-MM-DD')
            for k in json_dict.keys():
                if k in self.db_mapping.keys():
                    json_dict[self.db_mapping[k]] = json_dict[k]
                    json_dict.pop(k)
            self.model_mapping[int(section_number)].objects.filter(pk=id_variable_value).update(**json_dict)
            data = model_to_dict(Volunteer.objects.get(id=id_variable_value))
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
        sections = {}
        for section in self.xml_object.section:
            sections[section.attrib['position']] = Section(section, self)
        return sections


class DataPrep(object):
    def __init__(self, section, data):
        self.data = data
        self.section = section
        self.Question = Question
        
    def data_prep(self):
        if 'errors' in self.data.keys():
            self.section.errors = self.data['errors']

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
                                        multi_line[index][i].var_value = multi_data[index].__dict__[multi_line[index][i].variable]
                                        try:
                                            multi_line[index][i].var_id = multi_data[index].__dict__['id']
                                        except:
                                            pass
                                        multi_line[index][i].variable = multi_line[index][i].variable + '[]'
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
        q.var_value = data[q.variable]
