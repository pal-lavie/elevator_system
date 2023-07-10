# Elevator System
A simplified model of elevator system created using Python Django REST Framework using PostgresSQL deployed using Docker

## Setup 
Install Docker desktop on your system and start it.

Build the docker file using below commands and up the container
```
$ docker compose build
$ docker compose up -d
```
This will deploy the application on docker locally on port 8080

### Elevator Services

### Create elevator system with N elevators

```
curl --location 'http://localhost:8080/api/elevator-system/add/' \
--header 'Content-Type: application/json' \
--data '{
  "name": "system 2",
  "elevator_count": 2
}'
```

### Get elevator list by elevator system ID

```
curl --location 'http://localhost:8080/api/elevator/list/{system-id}' \
--header 'Content-Type: application/json'
```

Response
```
[
    {
        "id": 2,
        "elevator_serial_number": 42174,
        "is_active": false,
        "current_state": 4,
        "current_floor": 0,
        "is_door_closed": false,
        "elevator_system": 12
    },
    {
        "id": 3,
        "elevator_serial_number": 66136,
        "is_active": true,
        "current_state": 4,
        "current_floor": 0,
        "is_door_closed": true,
        "elevator_system": 12
    }
]
```


###  Mark a elevator as not working or in maintenance 

```
curl --location --request PUT 'http://localhost:8080/api/elevator/update/{elevator-serial-number}' \
--header 'Content-Type: application/json' \
--data '{
   
    "is_door_closed": false
    
}'
```

### Saves user request to the list of requests for a elevator

```
curl --location 'http://localhost:8080/api/elevator/{system-id}/request/{elevator-id}/add/' \
--header 'Content-Type: application/json' \
--data '{
  "source_floor": 2,
  "destination_floor": 8
}'
```

### Mark a elevator as not working or in maintenance

```
curl --location --request PUT 'http://localhost:8080/api/elevator/update/{elevator-serial-number}' \
--header 'Content-Type: application/json' \
--data '{
   
    "is_active": false
    
}'
```

###  Fetch all requests for a given elevator
```
curl --location 'http://localhost:8080/api/elevator-requests/list/{elevator-id}' \
--header 'Content-Type: application/json'
```

Response
```
[
    {
        "id": 1,
        "source_floor": 2,
        "destination_floor": 8,
        "active": true,
        "elevator": 2
    }
]
```

### Fetch if the elevator is moving up or down currently

```
curl --location 'http://localhost:8080/api/elevator/state/42174' \
--header 'Content-Type: application/json'
```

Response
```
[
    {
        "current_state": 4, # Current state: 4 Idle, directions are defined in enum file
        "current_floor": 0
    }
]
```