from django.db import models
from .enum.elevator_enums import CurrentState
# Create your models here.


class ElevatorSystem(models.Model):
    """ 
    Elevator system model that keeps track of the elevators associated with one system.
    It has an assigned name and primary key id.
    Here we will initialize the elevator count as well.
    """

    name = models.CharField(max_length=30)
    elevator_count =  models.IntegerField(default=0)


class Elevator(models.Model):
    """ 
    Single Elevator cm,lass identified by a serial number. Has a forieng key reference to the elevator system.
    Each elevator can be active or inactive, holds a current state - moving, idle and stopped, and current floor.
    A door flag is used to identify door state.
    Default current state would be IDLE = 4
    """

    elevator_system = models.ForeignKey(
        ElevatorSystem, on_delete=models.CASCADE)
    elevator_serial_number = models.IntegerField()
    is_active = models.BooleanField(default=True)
    current_state = models.IntegerField(default=4)
    current_floor = models.IntegerField(default=0)
    is_door_closed = models.BooleanField(default=False)

    def __str__(self) -> str:

        return str(self.elevator_serial_number)


class ElevatorRequest(models.Model):
    """
    This is a User Request Model to move elevator from a source floor to destination floor.
    active flag indicates the request state.
    """

    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    source_floor = models.IntegerField()
    destination_floor = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.elevator)
