from django.apps import AppConfig


class XpsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.xps'

    def ready(self):
        import apps.xps.receivers
