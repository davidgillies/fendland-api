import sqlsoup
import arrow
import cam_apps
import local_settings
from .models import Surgery
from cam_querysets import QuerySet


class CustomDataPrep(cam_apps.DataPrep):
    def __init__(self, section, data):
        super(CustomDataPrep, self).__init__(section, data)
        self.Question = cam_apps.Question

    def get_multi_data(self, table, id):
        # should really have a models based version for this too...?
        qs = QuerySet(table_name='volunteers', related_table='appointments', related_field='volunteers_id')
        qs.get(id)
        objs = qs.related_set()
        return objs

    def add_question_value(self, q):
        if q.variable == 'surgery':
            if local_settings.MODELS is True:
                q.var_value = self.data['surgeries']
            else:
                q.var_value = self.data['surgeries_id']
        elif q.variable == "diabetes":
            q.var_value = self.data['diabetes_diagnosed']
        else:
            q.var_value = self.data[q.variable]

        self.section.api[q.variable] = q.var_value


class CustomQuestion(cam_apps.Question):
    def __init__(self, question_object, app_object, section_object):
        self.surgeries = self.get_surgeries()
        super(CustomQuestion, self).__init__(question_object, app_object, section_object)

    def get_surgeries(self):
        # surgeries = db.surgeries.all()
        surgeries = QuerySet(table_name='surgeries').all()
        result = []
        for surgery in surgeries:
            result.append({'text': surgery['full_name'], 'value': surgery['id']})
        return result

    def get_options(self, option):
        return {'surgeries': self.surgeries}[option]


class CustomQuestionGroup(cam_apps.QuestionGroup):
    def __init__(self, question_group_object, app_object, section_object):
        super(CustomQuestionGroup, self).__init__(question_group_object, app_object, section_object)

    def set_question(self, item):
        question = CustomQuestion(item, self.app_object, self.section)
        self.question_group_objects.append(question)


class CustomSection(cam_apps.Section):
    def __init__(self, section_xml_object, app_object):
        super(CustomSection, self).__init__(section_xml_object, app_object)

    def set_question_group(self, item):
        question_group = CustomQuestionGroup(item, self.app_object, self)
        self.question_groups.append(question_group)
        self.section_objects.append(question_group)


class CustomApplication(cam_apps.Application):
    def __init__(self, name, xml):
        super(CustomApplication, self).__init__(name, xml)

    def get_sections(self):
        sections = {}
        for section in self.xml_object.section:
            sections[section.attrib['position']] = CustomSection(section, self)
        return sections

    def pre_process_keys(self, json_dict):
        if 'dob' in json_dict.keys():
                dob = arrow.get(json_dict['dob'], 'MMMM D, YYYY')
                json_dict['dob'] = dob.format('YYYY-MM-DD')
        return json_dict

    def post_process_keys(self, json_dict):
        if 'surgeries' in json_dict.keys():
            json_dict['surgeries'] = Surgery.objects.get(id=int(json_dict['surgeries']))
        return json_dict
        
    def search(self, search_term, section_number):
        if self.models:
            # data = model_to_dict(self.model_mapping[int(section_number)].objects.get(id=id_variable_value))
            data = self.model_mapping[int(section_number)].objects.filter(surname__contains=search_term) 
        else:
            queryset = QuerySet(table_name=self.get_table_name(section_number))
            data = queryset.filter('surname', search_term)
        return data
