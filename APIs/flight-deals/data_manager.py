import requests
import os

SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_ENDPOINT = "https://api.sheety.co/6ac059f3420e9cc262736256739041b4/flightDeals/prices"


class DataManager:
    """
    This class is responsible for talking to the Google Sheet
    methods in the class include getting and updating sheet data
    """
    def __init__(self):
        self.row_data = {}
    
    def get_sheet_data(self):
        """
        An instance method which gets the data available on the sheet
        The method returns a list of data contained within the sheet
        """
        headers = {
            "Authorization": SHEETY_BEARER_TOKEN
        }

        response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        response.raise_for_status()
        self.row_data = response.json()['prices']
        return self.row_data

    def update_sheet_data(self):
        """
        An instance method which updates IATA codes within the sheets
        """
        for data in self.row_data:
            headers = {
                "Authorization": SHEETY_BEARER_TOKEN
            }
            params = {
                "price": {
                    "iataCode": data['iataCode']
                    }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{data['id']}", json=params, headers=headers)

