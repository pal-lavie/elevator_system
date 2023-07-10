from rest_framework import serializers
from .models import Elevator, ElevatorRequest, ElevatorSystem


class ElevatorSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorSystem
        fields = "__all__"


class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = "__all__"
        
        
class ElevatorStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = fields = (
        'current_state', 
        'current_floor',
        )


class ElevatorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElevatorRequest
        fields = (
        'source_floor', 
        'destination_floor',
        )

class ElevatorRequestSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = ElevatorRequest
        fields = "__all__"