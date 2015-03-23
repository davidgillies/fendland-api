import cam_apps
import local_settings
import sqlsoup
from itertools import chain
from copy import deepcopy

db = sqlsoup.SQLSoup(local_settings.DATABASE)

def get_multi_data(table, id):
    db.table = db.entity(table)
    objs = db.table.filter(db.appointments.volunteers_id==id).all()
    return objs


def data_prep(section, data):
    try:
        for qg in section.section_objects:
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
                        multi_data = get_multi_data(multi_line[0].rendering_hints['multi'], data['id'])
                        multi_line_adder = []
                        for i in range(len(multi_data)):
                            multi_line_adder.append(deepcopy(multi_line))
                        multi_line = multi_line_adder
                        for index in range(len(multi_line)):
                            for i in range(len(multi_line[index])):
                                if isinstance(multi_line[index][i], cam_apps.Question):
                                    multi_line[index][i].var_value = multi_data[index].__dict__[multi_line[index][i].variable]
                                    try:
                                        multi_line[index][i].var_id = multi_data[index].__dict__['id']
                                    except:
                                        pass
                                    multi_line[index][i].variable = multi_line[index][i].variable + '[]'
                        multi_line = list(chain.from_iterable(multi_line))
                        multi_lines.append([multi_line, multi_index])
                elif isinstance(q, cam_apps.Question):
                    if q.variable == 'surgery':
                        q.var_value = data['surgeries_id']
                    elif q.variable == "diabetes":
                        q.var_value = data['diabetes_diagnosed']
                    else:
                        q.var_value = data[q.variable]
            for ml in multi_lines:
                qg.question_group_objects[ml[1]:ml[1]+(len(ml[0])/len(multi_data))] = ml[0]
        return section
    except:
        return section




class CustomQuestion(cam_apps.Question):
    def __init__(self, question_object):
        self.surgeries = self.get_surgeries()
        super(CustomQuestion, self).__init__(question_object)

    def set_options(self, item):
        if item.optionText.text == 'dynamic':
            self.template_args['options'] = self.get_options(item.optionValue.text)
        else:
            self.template_args['options'].append({'text': item.optionText.text, 'value': item.optionValue.text})

    def get_surgeries(self):
        surgeries = db.surgeries.all()
        result = []
        for surgery in surgeries:
            result.append({'text': surgery.full_name, 'value': surgery.id})
        return result

    def get_options(self, option):
        return {'surgeries': self.surgeries}[option]
        
    def set_options(self, item):
        if item.optionText.text == 'dynamic':
            self.template_args['options'] = self.get_options(item.optionValue.text)
        else:
            self.template_args['options'].append({'text': item.optionText.text, 'value': item.optionValue.text})


class CustomQuestionGroup(cam_apps.QuestionGroup):
    def set_question(self, item):
        question = CustomQuestion(item)
        self.question_group_objects.append(question)


class CustomSection(cam_apps.Section):
    def __init__(self, section_xml_object):
        super(CustomSection, self).__init__(section_xml_object)

    def set_question_group(self, item):
        question_group = CustomQuestionGroup(item)
        self.question_groups.append(question_group)
        self.section_objects.append(question_group)


class CustomApplication(cam_apps.Application):
    def __init__(self, name, xml):
        super(CustomApplication, self).__init__(name, xml)

    def get_sections(self):
        sections = {}
        for section in self.xml_object.section:
            sections[section.attrib['position']] = CustomSection(section)
        return sections
