import requests
from datetime import datetime

#response = requests.get(url="http://api.open-notify.org/iss-now.json")
#response = requests.get(url="http://api.open-notify.org/isss-now.json")
# print(response.status_code)
#
# if response.status_code == 404:
#     raise Exception("that resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("u are not authorized to access this data")







#response = requests.get(url="http://api.open-notify.org/isss-now.json")
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

#data = response.json()["name_of_key_tha_we_want"]
#data = response.json()["iss_position"]
# data = response.json()["iss_position"]["longitude"]
#print(data)





# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude,latitude)
#
# print(iss_position)





MY_LAT = 40.607271
MY_LONG = 22.961806



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()

data = response.json()

sunset = data["results"]["sunset"]
sunrise = data["results"]["sunrise"]


time_now = datetime.now()
print(time_now)

print("-------sunrise------------")
print(sunrise)
print(sunrise.split("T"))
print(sunrise.split("T")[1].split(":"))
print(sunrise.split("T")[1].split(":")[0])
print("-------sunset------------")
print(sunset)
print(sunset.split("T")[1].split(":")[0])
print("-------now------------")
print(time_now.hour)