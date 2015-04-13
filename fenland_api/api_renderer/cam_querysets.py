import local_settings
import sqlsoup
import datetime
from bunch import Bunch

db = sqlsoup.SQLSoup(local_settings.DATABASE)


class QuerySet(object):
    def __init__(self, query_dict={}, table_name='', sql='',
                 id_variable_value=''):
        self.query_dict = query_dict
        self.table_name = table_name
        self.sql = sql
        self.data = None
        self.id_variable_value = id_variable_value
        if self.table_name:
            self.table = db.entity(table_name)
        else:
            self.table = None
        self.objects = Bunch({'all': self.all, 'get': self.get,
                        'create': self.create, 'update': self.update,
                        'delete': self.delete})

    def all(self):
        pass

    def get(self):
        data = self.table.get(int(self.id_variable_value)).__dict__
        data.pop('_sa_instance_state')
        data['id'] = self.id_variable_value
        self.tidy(data)
        return data

    def create(self, query_dict):
        data = self.table.insert(**query_dict).__dict__
        data.pop('_sa_instance_state')
        db.commit()
        self.data = data
        return data

    def update(self, query_dict, id_variable_value):
        data = self.table.filter_by(id=int(id_variable_value)).update(query_dict)
        data = query_dict
        db.commit()
        self.data = data
        return

    def delete(self):
        instance = self.table.get(int(self.id_variable_value))
        db.delete(instance)
        db.commit()
        return

    def sql(self):
        # execute arbritrary sql
        pass

    def tidy(self, data):
        for k in data.keys():
            if isinstance(data[k], datetime.date):
                data[k] = str(data[k])
