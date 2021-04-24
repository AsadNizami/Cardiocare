from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = 'Cardiocare Users'

    def ready(self):
        import users.signals
