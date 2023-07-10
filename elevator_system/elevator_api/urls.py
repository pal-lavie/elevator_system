
from django.urls import path,include

from .views import *


urlpatterns=[

    # List all the elevator systems
    path('elevator-system/list/',ListElevatorSystem.as_view(), name='elevator-system-list'),
    
    # Create new elevator systems
    path('elevator-system/add/',CreateElevatorSystem.as_view(), name='elevator-system-add'),
    
    # List all the elevators with given system id
    path('elevator/list/<int:system_id>',ListElevators.as_view(), name="elevator-list"),
    
    # Change elevator status to active/inactive by elevator serial number
    path('elevator/update/<int:elevator_serial_number>',ChangeElevatorStatus.as_view(), name='elevator-update'),
    
    # Create elevator request
    path('elevator/<int:system_id>/elevator/<int:elevator_serial_number>/req/add-new/',CreateElevatorRequest.as_view(), name='elevator-request-add'),

    # List elevator requests by elevator id
    path('elevator-requests/list/<int:elevator_id>',ListElevatorRequests.as_view(),name='elevator-request-list' )
]