from lxml import objectify
import sqlsoup
import simplejson


class Application(object):
    def __init__(self, name, xml):
        self.name = name
        self.xml = xml
        self.xml_object = objectify.fromstring(self.xml)
        self.db = sqlsoup.SQLSoup('mysql+pymysql://david:david@localhost:3306/sm_db')

    def get_data(self, section_number, id_variable, id_variable_value):
        self.db.table = self.db.entity(self.get_table_name(section_number))
        data = self.db.table.get(int(id_variable_value)).__dict__
        data.pop('_sa_instance_state')
        return data

    def insert_data(self, section_number, id_variable, id_variable_value, body):
        self.db.table = self.db.entity(self.get_table_name(section_number))
        json_dict = simplejson.JSONDecoder().decode(body)
        data = self.db.table.insert(**json_dict).__dict__
        data.pop('_sa_instance_state')
        self.db.commit()
        return data

    def update_data(self, section_number, id_variable, id_variable_value, body):
        self.db.table = self.db.entity(self.get_table_name(section_number))
        json_dict = simplejson.JSONDecoder().decode(body)
        # problem: can't put a variable into this filter_by must be a
        # database column name
        data = self.db.table.filter_by(id=int(id_variable_value)).update(json_dict)
        data = json_dict
        self.db.commit()
        return data

    def delete_data(self, section_number, id_variable, id_variable_value):
        self.db.table = self.db.entity(self.get_table_name(section_number))
        instance = self.db.table.get(int(id_variable_value))
        self.db.delete(instance)
        self.db.commit()
        return

    def get_table_name(self, section_number):
        return 'volunteers'

    def get_section(self, section_number):
        return self.xml_object.section[int(section_number)]
