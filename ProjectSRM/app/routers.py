class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app':
            if model._meta.model_name == 'project':
                return 'default'
            elif model._meta.model_name == 'asset':
                return 'assets'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app':
            if model._meta.model_name == 'project':
                return 'default'
            elif model._meta.model_name == 'asset':
                return 'assets'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'app':
            if model_name == 'project':
                return db == 'default'
            elif model_name == 'asset':
                return db == 'assets'
        return None