
from django.urls import path,include

from .views import *


urlpatterns=[

    # List all the elevator systems
    path('elevator-system/list/',ListElevatorSystem.as_view(),name='elevator-system-list'),
    # Create new elevator systems
    path('elevator-system/add/',CreateElevatorSystem.as_view(),name='elevator-system-add'),
    # List all the elevators with given system id
    path('elevator/list/<int:id>',ListElevators.as_view(), name="elevator-list")
]