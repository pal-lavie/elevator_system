from django.apps import AppConfig


class ElevatorApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elevator_api'
    
    # def ready(self):
    #     from .elevator_dispatcher import DispatchElevator
    #     DispatchElevator().start()
