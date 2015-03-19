import cam_apps
import sqlsoup
from itertools import chain
from copy import deepcopy


def get_multi_data(table, id):
    db = sqlsoup.SQLSoup('mysql+pymysql://david:david@localhost:3306/sm_db')
    db.table = db.entity(table)
    objs = db.table.filter(db.appointments.volunteer_id==id).all()
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
                        multi_data = get_multi_data(multi_line[0].rendering_hints['multi'], data['volunteer_id'])
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
                        q.var_value = data['surgery_id']
                    elif q.variable == "diabetes":
                        q.var_value = data['diabetes_diagnosed']
                    else:
                        q.var_value = data[q.variable]
    
            for ml in multi_lines:
                qg.question_group_objects[ml[1]:ml[1]+(len(ml[0])/len(multi_data))] = ml[0]
        return section
    except:
        return section


class CustomFunctions(object):
    def __init__(self):
        self.db = sqlsoup.SQLSoup('mysql+pymysql://david:david@localhost:3306/sm_db')
        self.surgeries = self.get_surgeries()

    def get_surgeries(self):
        surgeries = self.db.surgeries.all()
        result = []
        for surgery in surgeries:
            result.append({'text': surgery.full_name, 'value': surgery.id})
        return result

    def get_options(self, option):
        return {'surgeries': self.surgeries}[option]
