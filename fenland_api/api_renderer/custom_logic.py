import cam_apps
import local_settings
import sqlsoup

db = sqlsoup.SQLSoup(local_settings.DATABASE)


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
