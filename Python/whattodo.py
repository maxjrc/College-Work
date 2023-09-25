import requests

url = "https://www.boredapi.com/api/activity"

# Sends a get request to the open api
info = requests.get(url)
# gets the json and stores
info_json = info.json()
print("Activity: " + info_json['activity'])
print("Type: " + info_json['type'])
print("Participants: ", int(info_json['participants']))
