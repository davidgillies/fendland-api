from lxml import objectify
import sqlsoup
import simplejson
from copy import deepcopy
import business_layer
import local_settings
import datetime

local_functions = business_layer.CustomFunctions()


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
    def __init__(self, question_object):
        self.question_objects = []
        self.title = question_object.attrib['position']
        self.variable = question_object.variable.varName.text
        self.var_value = None
        self.id = question_object.attrib['ID']
        self.position = question_object.attrib['position']
        self.rendering_hints = {}
        self.template = ''
        self.template_args = {'options': []}
        self.build_question(question_object)

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
            self.template_args['options'] = local_functions.get_options(item.optionValue.text)
        else:
            self.template_args['options'].append({'text': item.optionText.text, 'value': item.optionValue.text})

    def set_info(self, item):
        q_info = {}
        q_info['text'] = item.text
        q_info['cssClass'] = item.attrib['cssClass']
        self.question_objects.append(q_info)


# Tod dos:
# 1. set table and shownumber on the QuestionGroup object, they come from
# the renderingHints.
# 2. Is there anything that can be rendered entirely by a template to string
# that doesn't have any data...  First sections etc.  Does it help?

class QuestionGroup(MethodMixin):
    def __init__(self, question_group_object):
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
        question = Question(item)
        self.question_group_objects.append(question)


class Section(MethodMixin):
    def __init__(self, section_xml_object):
        self.section_xml_object = section_xml_object
        self.title = section_xml_object.title
        self.position = section_xml_object.attrib['position']
        self.info = []
        self.question_groups = []
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
        question_group = QuestionGroup(item)
        self.question_groups.append(question_group)
        self.section_objects.append(question_group)


class Application(object):
    def __init__(self, name, xml):
        self.name = name
        self.xml = xml
        self.xml_object = objectify.fromstring(self.xml)
        self.db = sqlsoup.SQLSoup(local_settings.DATABASE) # extract to business logic
        self.models = local_settings.MODELS
        self.custom = local_settings.CUSTOM
        self.mapping = local_settings.SECTION_MAPPING
        self.author = self.xml_object.author
        self.version_number = self.xml_object.versionNumber
        self.version_date = self.xml_object.versionDate
        self.title = self.xml_object.title
        self.studyname = self.xml_object.studyName
        self.sections = self.get_sections()

    def get_data(self, section, id_variable, id_variable_value):
        if self.models:
            pass
        else:
            self.db.table = self.db.entity(self.get_table_name(section))
            data = self.db.table.get(int(id_variable_value)).__dict__
            data.pop('_sa_instance_state')
            if self.custom:
                pass
            self.tidy(data)
        return data

    def tidy(self, data):
        for k in data.keys():
            if isinstance(data[k], datetime.date) :
                data[k] = str(data[k])

    def insert_data(self, section_number, id_variable, id_variable_value, body):
        if self.models:
            pass
        else:
            self.db.table = self.db.entity(self.get_table_name(section_number))
            json_dict = simplejson.JSONDecoder().decode(body)
            data = self.db.table.insert(**json_dict).__dict__
            # import prep data for fenland from fenland business logic
            data.pop('_sa_instance_state')
            self.db.commit()
            return data

    def update_data(self, section_number, id_variable, id_variable_value, body):
        if self.models:
            pass
        else:
            self.db.table = self.db.entity(self.get_table_name(section_number))
            json_dict = simplejson.JSONDecoder().decode(body)
            # problem: can't put a variable into this filter_by must be a
            # database column name
            data = self.db.table.filter_by(volunteer_id=int(id_variable_value)).update(json_dict)
            data = json_dict
            self.db.commit()
            return data

    def delete_data(self, section_number, id_variable, id_variable_value):
        if self.models:
            pass
        else:
            self.db.table = self.db.entity(self.get_table_name(section))
            instance = self.db.table.get(int(id_variable_value))
            self.db.delete(instance)
            self.db.commit()
            return

    def get_table_name(self, section_number):
        return self.mapping[int(section_number)] # add in a mapping from section to tables in business logic?

    def get_section(self, section_number):
        return deepcopy(self.sections[str(section_number)])

    def get_sections(self):
        sections = {}
        for section in self.xml_object.section:
            sections[section.attrib['position']] = Section(section)
        return sections
