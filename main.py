
# Campus Transport Allocation

print("==========================================")
print("       CAMPUS TRANSPORT ALLOCATION")
print("==========================================")

# Get number of routes
routes = int(input("Enter number of routes: "))

if routes <= 0:
    print("Invalid number of routes!")

else:

    # Initialize totals
    total_passengers = 0
    total_buses_required = 0
    total_buses_allocated = 0
    total_served = 0
    total_unserved = 0

    # Store route details
    route_details = []

    # Process each route
    for i in range(routes):

        print("\nRoute", i + 1)

        route_name = input("Enter route name: ")

        passengers = int(input("Enter passenger demand: "))

        capacity = int(input("Enter bus capacity: "))

        available_buses = int(
            input("Enter available buses: ")
        )

        # Validate input
        if passengers < 0 or capacity <= 0 or available_buses < 0:

            print("Invalid route details!")
            continue

        # Calculate required buses
        if passengers == 0:
            required_buses = 0
        else:
            required_buses = (
                passengers + capacity - 1
            ) // capacity

        # Allocate available buses
        allocated_buses = min(
            required_buses, available_buses
        )

        # Calculate served passengers
        served_passengers = min(
            passengers, allocated_buses * capacity
        )

        # Calculate unserved passengers
        unserved_passengers = (
            passengers - served_passengers
        )

        # Store route details
        route_details.append((
            route_name,
            passengers,
            capacity,
            required_buses,
            allocated_buses,
            served_passengers,
            unserved_passengers
        ))

        # Update totals
        total_passengers += passengers
        total_buses_required += required_buses
        total_buses_allocated += allocated_buses
        total_served += served_passengers
        total_unserved += unserved_passengers

    # Display route-wise report
    print("\n==========================================")
    print("          ROUTE ALLOCATION REPORT")
    print("==========================================")

    for route in route_details:

        print("\nRoute Name:", route[0])
        print("Passenger Demand:", route[1])
        print("Bus Capacity:", route[2])
        print("Buses Required:", route[3])
        print("Buses Allocated:", route[4])
        print("Passengers Served:", route[5])
        print("Unserved Passengers:", route[6])

        if route[6] == 0:
            print("Status: All passengers served")
        else:
            print("Status: Additional buses required")

    # Display final summary
    print("\n==========================================")
    print("           TRANSPORT SUMMARY")
    print("==========================================")

    print("Total Passenger Demand:", total_passengers)

    print("Total Buses Required:", total_buses_required)

    print("Total Buses Allocated:", total_buses_allocated)

    print("Total Passengers Served:", total_served)

    print("Total Unserved Passengers:", total_unserved)

    if total_unserved == 0:
        print("\nStatus: All passengers can be accommodated.")
    else:
        print("\nStatus: Additional buses are needed.")

    print("\n==========================================")
    print("          ALLOCATION COMPLETED")
    print("==========================================")
