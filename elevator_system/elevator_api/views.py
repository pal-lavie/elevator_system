from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Elevator, ElevatorRequest, ElevatorSystem
from .serializers import ElevatorSerializer, ElevatorRequestSerializer, ElevatorSystemSerializer
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
        id = self.kwargs['id']
        queryset = Elevator.objects.filter(elevator_system__id = id)

        return queryset


# class ElevatorRequest(generics.CreateAPIView):
#      m,
     