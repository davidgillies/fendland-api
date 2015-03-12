import cam_apps
import sqlsoup


def data_prep(section, data):
    try:
        for qg in section.section_objects:
            question_list = [q for q in qg.question_group_objects if isinstance(q, cam_apps.Question)]
            for q in question_list:
                if q.variable == 'surgery':
                    q.var_value = data['surgery_id']
                elif q.variable == "diabetes":
                    q.var_value = data['diabetes_diagnosed']
                else:
                    q.var_value = data[q.variable]
        return section
    except:
        return section
# should get any related data here...


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
