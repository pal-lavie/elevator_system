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