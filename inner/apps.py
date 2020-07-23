from django.apps import AppConfig


class InnerConfig(AppConfig):
    name = 'inner'

    def ready(self):
        import inner.signals
