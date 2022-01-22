"""
A simple habit tracker which consumes the pixela API
"""
import os
import requests
import datetime

TOKEN = os.environ.get("PIXELA_TOKEN")
USER = os.environ.get("PIXELA_USER_NAME")


# Create a user
# endpoint = "https://pixe.la/v1/users"
# params = {
#     "token": TOKEN,
#     "username": USER,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# 
# response = requests.post(url=endpoint, json=params)
# print(response.text)

# Create our first graph
# params = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Kilometre",
#     "type": "int",
#     "color": "sora"
# }
# 
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# 
# endpoint = f"https://pixe.la/v1/users/{USER}/graphs"
# response = requests.post(url=endpoint, json=params, headers=headers)
# print(response.text)

# Adding a pixel onto the graph
today = datetime.datetime.today()
today = today.date()
date = today.strftime("%Y%m%d")
# 
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# 
# params = {
#     "date": date,
#     "quantity": "7"
# }
# 
# pixel_endpoint = f"https://pixe.la/v1/users/{USER}/graphs/graph1"
# 
# response = requests.post(url=pixel_endpoint, json=params, headers=headers)
# print(response.text)

# Updating an already existing pixel on the graph
headers = {
    "X-USER-TOKEN": TOKEN
}

params = {
    "quantity": "15",
}

pixel_endpoint = f"https://pixe.la/v1/users/{USER}/graphs/graph1/{date}"

response = requests.put(url=pixel_endpoint, json=params, headers=headers)
print(response.text)
