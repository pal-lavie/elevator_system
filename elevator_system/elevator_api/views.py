from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Elevator, ElevatorRequest, ElevatorSystem
from .serializers import ElevatorSerializer, ElevatorRequestSerializer, ElevatorSystemSerializer, ElevatorRequestSerializerAll
import random


def randomnumber(N):
    
	minimum = pow(10, N-1)
	maximum = pow(10, N) - 1
	return random.randint(minimum, maximum)


# Find list of all systems
class ListElevatorSystem(generics.ListAPIView):
    
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer


# Create an elevator system with N elevators
class CreateElevatorSystem(generics.CreateAPIView):

    serializer_class = ElevatorSystemSerializer

    "Create System with N Elevators"
    def perform_create(self, serializer):
        serializer.save()
        
        elevator_count = serializer.data["elevator_count"]
        id = serializer.data["id"]
        for i in range(elevator_count):
            elevators = Elevator.objects.create(elevator_system_id = id, elevator_serial_number = randomnumber(5))
            print("elevators: ", elevators)
            elevators.save()

# Get elevator associated with specific system ID
class ListElevators(generics.ListAPIView):

    serializer_class = ElevatorSerializer

    def get_queryset(self):
        id = self.kwargs['system_id']
        queryset = Elevator.objects.filter(elevator_system__id = id)

        return queryset

# Change elevator status to active / inactive
class ChangeElevatorStatus(generics.UpdateAPIView):
    
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer
    lookup_field = 'elevator_serial_number'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Elevator status updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})


# Create requests for elevator
class CreateElevatorRequest(generics.CreateAPIView):
    
  serializer_class = ElevatorRequestSerializer

  def perform_create(self, serializer):
    system_id = self.kwargs['system_id']
    elevator_id = self.kwargs['elevator_id']

    queryset = Elevator.objects.filter(
      elevator_system__id = system_id,
      id = elevator_id
    )
    elevator_object = queryset[0]

    serializer.save(elevator = elevator_object)
    

# Fetch all requests for a given elevator
class ListElevatorRequests(generics.ListAPIView):
    
    serializer_class = ElevatorRequestSerializerAll

    def get_queryset(self):
        system_id = self.kwargs['elevator_id']
        queryset = ElevatorRequest.objects.filter(elevator__id = system_id)

        return queryset

# Fetch next destination for a given elevator
class GetElevatorNextDestination(generics.ListAPIView):
    
    serializer_class = ElevatorRequestSerializer

    def get_queryset(self):
        elevator_id = self.kwargs['elevator_id']
        queryset = ElevatorRequest.objects.filter(elevator__id = elevator_id).order_by("-id")

        return queryset