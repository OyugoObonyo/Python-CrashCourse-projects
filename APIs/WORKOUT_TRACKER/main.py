"""
Consuming various APIs to record work out information
on google sheets
"""
import requests
import datetime
import os

APP_ID = os.environ.get['APP_ID']
API_KEY = os.environ.get['API_KEY']
WEIGHT = 70
HEIGHT = 176
AGE = 20
GENDER = "male"


endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
prompt = input("Tell me what exercices you did today: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
    "query": prompt,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=endpoint, json=params, headers=headers)
result = response.json()
exercises = result['exercises']

SHEETY_ENDPOINT = "https://api.sheety.co/6ac059f3420e9cc262736256739041b4/myWorkouts/workouts"
today = datetime.datetime.now()

# Convert date and time to a more readable format
date = today.date().strftime('%d/%m/%Y')
time = today.time().strftime('%H:%M:%S')

for exercise in exercises:
    headers = {
        "Authorization": f"Bearer {os.environ.get['BEARER_ID']}"
    }

    parameters = {
        "workout": {
                "date": date,
                "time": time,
                "exercise": exercise['name'].title(),
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories']
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=parameters, headers=headers)
