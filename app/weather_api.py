import requests

def get_coordinates(city):
    geocode_url = f"https://nominatim.openstreetmap.org/search?city={city}&format=json&limit=1"
    response = requests.get(geocode_url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
    return None, None

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None