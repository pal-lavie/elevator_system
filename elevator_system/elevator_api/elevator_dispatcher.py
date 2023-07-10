from .models import Elevator,ElevatorRequest,ElevatorSystem
from threading import Thread
from .enum.elevator_enums import Floor, CurrentState
import time

class DispatchElevator(Thread):
    
    # dispatch threads to source elevators
    def run(self):
        print("hereeeeee............")
        while True:
            time.sleep(5)
            dispatch()


    def dispatch():
        print("in dispatcher..........")
        systems = ElevatorSystem.objects.all()

        for system in systems:

            active_elevators = Elevator.objects.filter(
            elevator_system = system,
            is_active = True,
            )

            for elevator in active_elevators:
                requests = ElevatorRequest.objects.filter(
                    elevator = elevator,
                    active = True
                )
                
                for request in requests:
                    source = request.requested_floor
                    destination = request.destination_floor
                    
                    # Check validity of request
                    
                    # source is same as destination
                    if source == destination:
                        request.active = False
                        request.save()
                        continue
                    
                    # source and/or destination value are beyond given floors
                    if source > Floor.MAX.value or source < Floor.MIN.value or destination > Floor.MAX.value or destination < Floor.MIN.value:
                        request.active = False
                        request.save()
                        continue
                        
                    
                    # Start processing valid request
                    
                    # Open the door
                    elevator.is_door_closed = True
                    
                    
                    # Get the elevator to the source
                    while source != elevator.current_floor and elevator.current_floor <= Floor.MAX.value and elevator.current_floor >= Floor.MIN.value:
                        if source > elevator.current_floor:
                            elevator.current_state = CurrentState.MOVING_UP.value
                            elevator.current_floor = elevator.current_floor + 1
                        elif source < elevator.current_floor:
                            elevator.current_state = CurrentState.MOVING_DOWN.value
                            elevator.current_floor = elevator.current_floor - 1
                        
                        elevator.save()
                    
                    
                    # Elevator has reached the source, now move to destination
                    
                    # Open the door
                    elevator.is_door_closed = False
                    
                    
                    # Close the door
                    elevator.is_door_closed = True
                    current = source
                    while current != destination and current <= Floor.MAX.value and current >= Floor.MIN.value:
                        if source > elevator.current_floor:
                            elevator.current_state = CurrentState.MOVING_UP.value
                            elevator.current_floor = elevator.current_floor + 1
                        elif source < elevator.current_floor:
                            elevator.current_state = CurrentState.MOVING_DOWN.value
                            elevator.current_floor = elevator.current_floor - 1
                        
                        elevator.save()
                    
                    # Set elevator current floor as detination and current state as STOPPED
                    elevator.current_floor = destination
                    elevator.current_state = CurrentState.STOPPED.value
                    # Open the door
                    elevator.is_door_closed = False
                    elevator.save()
                    
                    # Update the request as processed/inactive and save
                    request.active = False
                    request.save()
                
                    