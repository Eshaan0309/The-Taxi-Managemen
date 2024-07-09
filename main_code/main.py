class Taxi:
 def __init__(self, taxi_id, driver_name, current_location):
 self.taxi_id = taxi_id 
 self.driver_name = driver_name
 self.current_location = current_location
 self.available = True
class Passenger:
 def __init__(self, passenger_id, name, contact_info):
 self.passenger_id = passenger_id
 self.name = name
 self.contact_info = contact_info
class Booking:
 def __init__(self, booking_id, pickup_location, dropoff_location, passenger,
taxi=None):
 self.booking_id = booking_id
 self.pickup_location = pickup_location
 self.dropoff_location = dropoff_location
 self.passenger = passenger
 self.taxi = taxi
 self.completed = False
class TaxiManagementSystem:
 def __init__(self):
 self.taxis = []
 self.bookings = []
 def add_taxi(self, taxi):
 self.taxis.append(taxi)
 def book_taxi(self, pickup_location, dropoff_location, passenger):
 available_taxis = [taxi for taxi in self.taxis if taxi.available]
 if not available_taxis:
 print("Sorry, no taxis available at the moment.")
 return None
 taxi = available_taxis[0]
 taxi.available = False
 booking_id = len(self.bookings) + 1
 booking = Booking(booking_id, pickup_location, dropoff_location, passenger,
taxi)
 self.bookings.append(booking)
 print(f"Booking successful! Taxi {taxi.taxi_id} is on its way.")
 return booking
 def complete_booking(self, booking_id):
 for booking in self.bookings:
 if booking.booking_id == booking_id:
 booking.taxi.available = True
 booking.completed = True
 print(f"Booking {booking_id} completed. Thank you for riding with
us!")
 return
 print("Booking not found.")
if __name__ == "__main__": 
    # Create Taxi Management System
 tms = TaxiManagementSystem()
 # Add Taxis
 t1 = Taxi("T001", "John Doe", "Central Station")
 t2 = Taxi("T002", "Jane Smith", "City Mall")
 t3 = Taxi("T003", "David Brown", "Airport")
 tms.add_taxi(t1)
 tms.add_taxi(t2)
 tms.add_taxi(t3)
 # Book a Taxi
 passenger = Passenger("P001", "Alice", "123-456-7890")
 booking1 = tms.book_taxi("Central Park", "Downtown", passenger)
 booking2 = tms.book_taxi("Airport", "Hotel", passenger)