class Flight():

    def __init__(self, flight_number, source, destination, number_of_available_seats):
        self.flight_number = flight_number
        self.source = self.short_and_capital(source)
        self.destination = self.short_and_capital(destination)
        self.number_of_available_seats = number_of_available_seats

    # Accessors
    def get_flight_number(self):
        return self.flight_number

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    def get_number_of_available_seats(self):
        return self.number_of_available_seats

    # Mutators
    def set_source(self, source):
        self.source = self.short_and_capital(source)

    def set_destination(self, destination):
        self.destination = self.short_and_capital(destination)

    def set_number_of_available_seats(self, number_of_available_seats):
        self.number_of_available_seats = number_of_available_seats

    # Other methods
    def reserve(self, number_of_seats):
        if(self.number_of_available_seats >= number_of_seats):
            self.number_of_available_seats -= number_of_seats

    def cancel(self, number_of_seats):
        self.number_of_available_seats += number_of_seats

    def to_string(self):
        print("Flight No:", self.get_flight_number(),\
              "\nFrom:", self.get_source(),\
              "\nTo:", self.get_destination())

    def equal(self, flight2):
        return self.get_flight_number() == flight2.get_flight_number()

    def short_and_capital(self, name):
        return name[:3]


flight= Flight(1234,"Tirana","Munich", 45)
flight.to_string()
flight.set_destination("Memmingen")
flight.set_source("Kukes")
flight.set_number_of_available_seats(50)
flight.to_string()

print("Number of available seats:", flight.get_number_of_available_seats())
flight.reserve(5)
print("Number of available seats:", flight.get_number_of_available_seats())
flight.reserve(50)
print("Number of available seats:", flight.get_number_of_available_seats())
flight.cancel(3)
print("Number of available seats:", flight.get_number_of_available_seats())

flight2 = Flight(1234,"Tirana","Munich", 45)
print(flight.equal(flight2))
flight3 = Flight(2000, "Kukes", "Memmingen", 50)
print(flight.equal(flight3))