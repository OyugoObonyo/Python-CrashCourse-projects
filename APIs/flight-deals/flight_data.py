class FlightData:
    """
    This class organizes flight data as per the required details
    """
    def __init__(self, price, source_city, source_airport, dest_city, dest_airport):
        """
        Initializes flight with the required data
        """
        self.source_city = source_city
        self.source_airport = source_airport
        self.dest_city = dest_city
        self.dest_airport = dest_airport
        self.price = price
        # self.departure = departure
        # self.arrival = arrival