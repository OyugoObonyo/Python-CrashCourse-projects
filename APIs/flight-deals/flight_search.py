import requests
import datetime
from dateutil.relativedelta import relativedelta
from flight_data import FlightData
import os

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iata_code(self, city):
        """
        An instance method tasked with getting the iatacode of a city
        Takes a city name as arguement and returns the city's IATA code
        """
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        
        query = {
            "term": city,
            "location_types":"city"
        }
        
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=query, headers=headers)
        response.raise_for_status()
        code = response.json()['locations'][0]['code']
        return code

    def get_flight_details(self, origin, destination):
        """
        Gets particular details about cheapest flight found flight.
        """
        date_today = datetime.datetime.now().date().strftime("%d/%m/%Y")
        after_six_months = (datetime.datetime.now().date() + relativedelta(months=+6)).strftime("%d/%m/%Y")
        header = {
            "apikey": TEQUILA_API_KEY
        }
        query = {
            "fly_from": f"city:{origin}",
            "fly_to": f"city:{destination}",
            "date_from": date_today,
            "date_to": after_six_months,
            "one_for_city": 1,
            "curr": "KES",
        
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/search", params=query, headers=header)
        response.raise_for_status
        # Pick first index in case of flights with similar prices 
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"There are currently no flights to {destination}")
            return None
        # Come back and check on what is happening to arrival and deprt. dates
        flight_details = FlightData(
            price = data['price'], 
            source_city = data['cityCodeFrom'],
            source_airport = data['flyFrom'],
            dest_city = data['cityCodeTo'],
            dest_airport = data['flyTo']
        )
        return flight_details
