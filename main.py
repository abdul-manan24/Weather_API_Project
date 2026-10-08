import requests

def get_weather_data(api_key, location, start_date=None, end_date=None):

    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"

    if start_date and end_date:
        url = f"{base_url}{location}/{start_date}/{end_date}"
    elif start_date:
        url = f"{base_url}{location}/{start_date}"
    else:
        url = f"{base_url}{location}"

    params = {

        "unitGroup": "metric",
        "key": api_key,
        "contentType": "json"

    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        weather_data = response.json()
        return weather_data

    except requests.exceptions.HTTPError as http_err:
        print("Http error occurred:", {http_err})
    except Exception as err:
        print(f"Error occurred: {err}")

API_Key = "RFQ3B5P7QC78XW9VXDX7ZMS56"
Location = input("Enter Location: ")

data = get_weather_data(API_Key, Location)

if data:
    print(f"Weather for: {data.get('resolvedAddress')}")
    current_conditions = data.get('currentConditions', {})
    print(f"Current Temp: {current_conditions.get('temp')}°C")
    print(f"Conditions: {current_conditions.get('conditions')}")