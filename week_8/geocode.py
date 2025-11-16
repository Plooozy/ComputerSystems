import requests # library to send HTTP requests
import time # Python time library to get time
from datetime import datetime # For better format of date

# read API key from "my_api.txt" which is located in tha same directory
# or you can just write like *API_KEY = "your api key here"*
with open("my_api.txt", "r") as f:
    API_KEY = f.read().strip()

# function that gets coordinates
def geocode_address(address: str, api_key: str):
    # address for looking up for
    # api_key your Google API key
    url = "https://maps.googleapis.com/maps/api/geocode/json" # URL Geocoding API
    params = {"address": address, "key": api_key} # parameters of request
    try:
        # sending GET request to Google API with timeout 10 seconds
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()  # check for errors HTTP (404, 500 etc)
        data = resp.json()
    except requests.exceptions.RequestException as e:
        # if there is any mistake we return None with text of error
        return None, f"HTTP error: {e}"

    # checking API status
    status = data.get("status")
    if status != "OK":
        return None, status

    # getting result list
    results = data.get("results")
    if not results:
        return None, "NO_RESULTS"

    # we take first result (Google API returns list of results)
    first = results[0]
    formatted = first.get("formatted_address") # we change format of address
    location = first.get("geometry", {}).get("location", {}) # dictionary with lat lng
    lat = location.get("lat") # latitude
    lng = location.get("lng") # longitude

    # if there is nothing, returnn error
    if formatted is None or lat is None or lng is None:
        return None, "INCOMPLETE_RESULT"

    # return dictionary with address lat and lng and status OK
    return {"address": formatted, "lat": lat, "lng": lng}, "OK"

# function that gets local time by coordinates
def get_local_time(lat: float, lng: float, api_key: str):
    timestamp = int(time.time()) # current local time
    url = "https://maps.googleapis.com/maps/api/timezone/json" # URL Time Zone API
    params = {
        "location": f"{lat},{lng}", # coordinates
        "timestamp": timestamp,
        "key": api_key
    }
    try:
        # GET request to Google Time Zone API
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        return None, None, f"HTTP error: {e}"

    if data.get("status") != "OK":
        return None, None, data.get("status")

    # rawOffset - standard time offset from UTC in seconds
    # dstOffset - daylight saving time offset
    offset = data["rawOffset"] + data["dstOffset"]

    # calculate local time (UTC + offset)
    local_time = datetime.utcfromtimestamp(timestamp + offset)
    tz_id = data["timeZoneId"] # time zone name, for example "Europe/Moscow"
    return local_time, tz_id, "OK"

# main cycle
print("Введите адрес. Для выхода напишите 'exit'.\n")

while True:
    address_input = input("Адрес: ")
    if address_input.lower() == "exit":
        print("Выход из программы.")
        break

    # we obtain coordinates via Geocoding API
    geo_result, geo_status = geocode_address(address_input, API_KEY)
    if geo_status != "OK":
        print("Ошибка геокодинга:", geo_status)
        print("-" * 40)
        continue

    # we save the latitude, longitude and normal format for address
    lat, lng = geo_result["lat"], geo_result["lng"]
    formatted_address = geo_result["address"]

    # getting local time via Time Zone API
    local_time, tz_id, time_status = get_local_time(lat, lng, API_KEY)
    if time_status != "OK":
        print("Ошибка определения времени:", time_status)
        print("-" * 40)
        continue

    # printing the results
    print(f"\nАдрес: {formatted_address}")
    print(f"Координаты: {lat}, {lng}")
    print(f"Часовой пояс: {tz_id}")
    print(f"Местное время: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)
