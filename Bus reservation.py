# Bus Reservation System

# Bus details - A list of buses available
buses = [
    {"id": 1, "name": "Bus A", "seats": 10},
    {"id": 2, "name": "Bus B", "seats": 15},
    {"id": 3, "name": "Bus C", "seats": 12},
]

# Display available buses
print("Welcome to the Online Bus Reservation System")
print("Available buses:")
for bus in buses:
    print(f"{bus['id']}. {bus['name']} - {bus['seats']} seats available")

# Ask user to choose a bus
bus_id = int(input("Enter the bus number you want to reserve: "))

# Check if the selected bus exists
bus_selected = None
for bus in buses:
    if bus['id'] == bus_id:
        bus_selected = bus
        break

if bus_selected is None:
    print("Invalid bus selection!")
else:
    # Ask how many tickets to book
    tickets_to_book = int(input(f"How many tickets would you like to book for {bus_selected['name']}? "))

    # Check if enough seats are available
    if tickets_to_book > bus_selected['seats']:
        print(f"Sorry, only {bus_selected['seats']} seats are available.")
    else:
        # Reserve the tickets
        bus_selected['seats'] -= tickets_to_book
        print(f"Reservation successful! {tickets_to_book} ticket(s) booked for {bus_selected['name']}.")

        # Get passenger details
        for i in range(tickets_to_book):
            name = input(f"Enter name for passenger {i+1}: ")
            age = int(input(f"Enter age for passenger {i+1}: "))
            print(f"Passenger {i+1} details: Name: {name}, Age: {age}")

        print(f"{tickets_to_book} ticket(s) successfully reserved on {bus_selected['name']}!")
        print(f"Remaining seats on {bus_selected['name']}: {bus_selected['seats']}")
