from django.apps import AppConfig


class AcountappConfig(AppConfig):
    name = 'acountapp'
    def ready(self):
        import account.signals
