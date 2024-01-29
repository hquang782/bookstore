# category/routers.py
class CategoryRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ["product", "category"]:
            return "mongo"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ["product", "category"]:
            return "mongo"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in ["product", "category"] or obj2._meta.app_label in [
            "product",
            "category",
        ]:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in ["product", "category"]:
            return db == "mongo"
        return None
