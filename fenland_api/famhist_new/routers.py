class PlayRouter(object):
    """
          A router to control all database operations on models in
          the api_renderer application
    """

    def db_for_read(self, model, **hints):
        """
        Point all operations on api_renderer models to 'db4'
        """
        if model._meta.app_label == 'famhist_new':
            return 'db4'
        return None

    def db_for_write(self, model, **hints):
        """
        Point all operations on api_renderer models to 'other'
        """
        if model._meta.app_label == 'famhist_new':
            return 'db4'
        return None

    def allow_syncdb(self, db, model):
        """
        Make sure the 'api_renderer' app only appears on the 'other' db
        """
        if db == 'db4':
            return model._meta.app_label == 'famhist_new'
        elif model._meta.app_label == 'famhist_new':
            return False
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_list = ('db4')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True
