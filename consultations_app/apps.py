from django.apps import AppConfig


class ConsultationsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'consultations_app'

    def ready(self):
        """
        Ready - это метод, который вызывается при загрузке приложения.
        Мы можем здесь подписываться на сигналы.
        """
        import consultations_app.signals
