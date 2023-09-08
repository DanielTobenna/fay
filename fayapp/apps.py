from django.apps import AppConfig


class FayappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fayapp'

    def ready(self):
    	import fayapp.signals
