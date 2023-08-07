from django.apps import AppConfig


class CarpartsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CarParts'

    def ready(self):
        result = super().ready()
        from CarParts import signals

        return result