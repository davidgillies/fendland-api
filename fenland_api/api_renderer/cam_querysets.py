import local_settings
import sqlsoup
import datetime
from bunch import Bunch

db = sqlsoup.SQLSoup(local_settings.DATABASE)


class QuerySet(object):
    def __init__(self, query_dict={}, table_name='', sql='',
                 id_variable_value='', related_table=''):
        self.query_dict = query_dict
        self.table_name = table_name
        self.sql = sql
        self.related_table = related_table
        self.db = db
        self.data = None
        self.id_variable_value = id_variable_value
        if self.table_name:
            self.table = self.db.entity(table_name)
        else:
            self.table = None
        self.objects = Bunch({'all': self.all, 'get': self.get,
                              'create': self.create,
                              'update': self.update, 'delete': self.delete,
                              'sql_execute': self.sql_execute, 'filter': self.filter,
                              'related_set': self.related_set})

    def all(self):
        records = self.table.all()
        result = []
        for record in records:
            rec = record.__dict__
            rec.pop('_sa_instance_state')
            result.append(rec)
        return result

    def get(self, id_variable_value=None):
        if id_variable_value == None:
            id_variable_value = self.id_variable_value
        data = self.table.get(int(id_variable_value)).__dict__
        data['id'] = id_variable_value
        self.id_variable_value = id_variable_value
        self.tidy(data)
        return data

    def create(self, query_dict):
        data = self.table.insert(**query_dict).__dict__
        data.pop('_sa_instance_state')
        db.commit()
        self.id_variable_value = data[u'id']
        self.data = data
        return data

    def update(self, query_dict, id_variable_value):
        self.id_variable_value = int(id_variable_value)
        data = self.table.filter_by(id=int(id_variable_value)).update(query_dict)
        data = query_dict
        db.commit()
        self.data = data
        return

    def delete(self, id_variable_value):
        instance = self.table.get(int(id_variable_value))
        self.id_variable_value = id_variable_value
        db.delete(instance)
        db.commit()
        return

    def sql_execute(self, sql_string):
        rp = db.execute(sql_string)
        rows = rp.fetchall()
        result = []
        for row in rows:
            rec = self.row2dict(row)
            result.append(rec)
        return result

    def tidy(self, data):
        data.pop('_sa_instance_state')
        for k in data.keys():
            if isinstance(data[k], datetime.date):
                data[k] = str(data[k])
 
    def filter(self, field, like, order=None):
        result = self.sql_execute("""select * from %s where %s like '%%%s%%';""" % (self.table_name, field, like))
        return result

    def related_set(self, related_table=None, field='id'):
        if related_table == None:
            related_table = self.related_table
        result = self.sql_execute("""select * from %s where %s = %s;""" % (related_table, field, int(self.id_variable_value)))
        return result

    def row2dict(self, row):
        d = {}
        for key, value in row.items():
            d[key] = value
        return d
