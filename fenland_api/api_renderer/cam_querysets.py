import local_settings
import sqlsoup
import datetime

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

    def all(self):
        pass

    def get(self):
        data = self.table.get(int(self.id_variable_value)).__dict__
        data.pop('_sa_instance_state')
        data['id'] = self.id_variable_value
        self.tidy(data)
        return data

    def create(self):
        data = self.table.insert(**self.query_dict).__dict__
        data.pop('_sa_instance_state')
        db.commit()
        self.data = data
        return

    def update(self):
        data = self.table.filter_by(id=int(self.id_variable_value)).update(self.query_dict)
        data = self.query_dict
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

    def objects(self):
        pass

    def tidy(self, data):
        for k in data.keys():
            if isinstance(data[k], datetime.date):
                data[k] = str(data[k])
