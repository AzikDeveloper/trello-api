from django.apps import AppConfig


class BoardlistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'boardlist'

    def ready(self):
        import boardlist.signals
