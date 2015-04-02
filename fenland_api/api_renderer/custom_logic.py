import cam_apps
import local_settings
import sqlsoup


db = sqlsoup.SQLSoup(local_settings.DATABASE)


class CustomDataPrep(cam_apps.DataPrep):
    def __init__(self, section, data):
        super(CustomDataPrep, self).__init__(section, data)
        self.Question = cam_apps.Question
        print "Data: %s" % data

    def get_multi_data(self, table, id):
        db.table = db.entity(table)
        objs = db.table.filter(db.appointments.volunteers_id==id).all()
        return objs

    def add_question(self, q):
        if q.variable == 'surgery':
            q.var_value = self.data['surgeries_id']
        elif q.variable == "diabetes":
            q.var_value = self.data['diabetes_diagnosed']
        else:
            q.var_value = self.data[q.variable]


class CustomQuestion(cam_apps.Question):
    def __init__(self, question_object, app_object):
        self.surgeries = self.get_surgeries()
        super(CustomQuestion, self).__init__(question_object, app_object)

    def get_surgeries(self):
        surgeries = db.surgeries.all()
        result = []
        for surgery in surgeries:
            result.append({'text': surgery.full_name, 'value': surgery.id})
        return result

    def get_options(self, option):
        return {'surgeries': self.surgeries}[option]


class CustomQuestionGroup(cam_apps.QuestionGroup):
    def __init__(self, question_group_object, app_object):
        super(CustomQuestionGroup, self).__init__(question_group_object, app_object)

    def set_question(self, item):
        question = CustomQuestion(item, self.app_object)
        self.question_group_objects.append(question)


class CustomSection(cam_apps.Section):
    def __init__(self, section_xml_object, app_object):
        super(CustomSection, self).__init__(section_xml_object, app_object)

    def set_question_group(self, item):
        question_group = CustomQuestionGroup(item, self.app_object)
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
