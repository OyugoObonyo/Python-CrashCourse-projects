from data_manager import DataManager
from flight_search import  FlightSearch
from notification_manager import NotificationManager

ORIGIN = "NBO"
# Populate Google sheet copy
flight_sheet =  DataManager()
sheet_data = flight_sheet.get_sheet_data()

# Get IATA code
flight_search = FlightSearch()
for row in sheet_data:
    if row['iataCode'] == "":
        row['iataCode'] = flight_search.get_iata_code(row['city'])

# Update IATA code on google sheet
flight_sheet.update_sheet_data()

# Get cheap flights
for row in sheet_data:
    flights = flight_search.get_flight_details(ORIGIN, row['iataCode'])
    if flights and flights.price <= row['lowestPrice']:
        notification = NotificationManager(flights.price, ORIGIN, flights.source_airport, flights.dest_city, flights.dest_airport)
        notification.send_email()
    else:
        continue
