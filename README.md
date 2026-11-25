# Campus_Transport
# Campus Transport Allocation

## Python Activity-Based Learning

### Student Details

- **Name:** DURGA SURYA PRAVALLIKA
- **Roll Number:** N26V01A0383
- **Branch:** CSE
- **Section:** 5
- **Programming Language:** Python

---

## 1. Problem Statement

Campus Transport Allocation is a Python-based program that determines the number of buses required for different campus transport routes.

The program considers passenger demand, bus capacity and available buses for each route. It calculates the required buses, allocated buses, passengers served and unserved passengers.

It also generates a final transport summary to identify routes that need additional buses.

## 2. Objectives

- To calculate the number of buses required for each route.
- To consider the seating capacity of each bus.
- To compare required buses with available buses.
- To calculate the number of passengers served.
- To identify unserved passengers.
- To generate a route-wise transport report.
- To calculate the total number of buses required and allocated.

## 3. Assumptions

1. The number of routes must be greater than zero.
2. Passenger demand must be a non-negative integer.
3. Bus capacity must be greater than zero.
4. Available buses must be a non-negative integer.
5. Each bus can carry passengers up to its seating capacity.
6. All buses have the same capacity within a particular route.
7. Buses are allocated separately to each route.
8. A passenger is considered served when a seat is available.
9. Invalid route records are skipped.
10. The remaining passengers are considered unserved when available bus capacity is insufficient.

## 4. Formulas

### Number of Buses Required

Required Buses = Ceiling (Passenger Demand / Bus Capacity)

### Number of Buses Allocated

Allocated Buses = Minimum of Required Buses and Available Buses.

### Passengers Served

Passengers Served = Minimum of Passenger Demand and (Allocated Buses × Bus Capacity).

### Unserved Passengers

Unserved Passengers = Passenger Demand - Passengers Served.

## 5. Algorithm

1. Start the program.
2. Enter the number of transport routes.
3. Initialize total passenger demand and bus counters.
4. Create an empty list to store route details.
5. Repeat the following steps for every route:
   - Enter route name.
   - Enter passenger demand.
   - Enter bus capacity.
   - Enter available buses.
6. Validate the entered values.
7. Calculate the required number of buses.
8. Calculate the number of buses allocated.
9. Calculate the passengers served.
10. Calculate the unserved passengers.
11. Store the route details in a list.
12. Update the overall totals.
13. Display the route-wise allocation report.
14. Display total passenger demand.
15. Display total buses required and allocated.
16. Display total served and unserved passengers.
17. Identify whether additional buses are needed.
18. Stop the program.

## 6. Pseudocode

```text
START

INPUT number_of_routes

IF number_of_routes <= 0
    DISPLAY Invalid number of routes

ELSE

    INITIALIZE all totals to zero

    FOR each route

        INPUT route_name
        INPUT passenger_demand
        INPUT bus_capacity
        INPUT available_buses

        IF passenger_demand < 0
           OR bus_capacity <= 0
           OR available_buses < 0

            DISPLAY Invalid route details

        ELSE

            IF passenger_demand == 0
                required_buses = 0
            ELSE
                required_buses =
                CEILING(passenger_demand / bus_capacity)
            END IF

            allocated_buses =
            MIN(required_buses, available_buses)

            served_passengers =
            MIN(passenger_demand,
            allocated_buses * bus_capacity)

            unserved_passengers =
            passenger_demand - served_passengers

            STORE route details

            UPDATE total values

        END IF

    END FOR

    DISPLAY route allocation report

    DISPLAY total passengers
    DISPLAY total buses required
    DISPLAY total buses allocated
    DISPLAY total passengers served
    DISPLAY total unserved passengers

    IF total_unserved == 0
        DISPLAY All passengers can be accommodated
    ELSE
        DISPLAY Additional buses are needed
    END IF

END IF

STOP
```

## 7. Python Source Code

**File name:** `campus_transport.py`

The complete Python implementation is available in this folder.

## 8. Test Cases

| Test Case | Demand | Capacity | Available Buses | Expected Result |
|---|---:|---:|---:|---|
| 1 | 120 | 50 | 3 | 3 buses, 0 unserved |
| 2 | 180 | 60 | 2 | 3 required, 60 unserved |
| 3 | 45 | 50 | 1 | 1 bus, 0 unserved |
| 4 | 0 | 50 | 2 | 0 buses required |
| 5 | 100 | 0 | 2 | Invalid capacity |
| 6 | -20 | 50 | 2 | Invalid passenger demand |
| 7 | 100 | 50 | 0 | 100 unserved |

## 9. Expected Output

```text
CAMPUS TRANSPORT ALLOCATION

ROUTE ALLOCATION REPORT

Route A
Passenger Demand: 120
Bus Capacity: 50
Buses Required: 3
Buses Allocated: 3
Passengers Served: 120
Unserved Passengers: 0

Route B
Passenger Demand: 180
Bus Capacity: 60
Buses Required: 3
Buses Allocated: 2
Passengers Served: 120
Unserved Passengers: 60

Route C
Passenger Demand: 45
Bus Capacity: 50
Buses Required: 1
Buses Allocated: 1
Passengers Served: 45
Unserved Passengers: 0

TRANSPORT SUMMARY

Total Passenger Demand: 345
Total Buses Required: 7
Total Buses Allocated: 6
Total Passengers Served: 285
Total Unserved Passengers: 60

Status: Additional buses are needed.

ALLOCATION COMPLETED
```

## 10. Conclusion

The Campus Transport Allocation program successfully calculates the number of buses required for multiple routes based on passenger demand and bus capacity.

It compares the required buses with available buses, calculates served and unserved passengers and identifies routes that need additional buses.

This project helps us understand Python variables, lists, tuples, loops, conditional statements, arithmetic operators and built-in functions such as min().

It also demonstrates how Python can be used to solve real-world campus transportation problems.

---

**Project:** Python Activity-Based Learning  
**Topic:** Campus Transport Allocation
