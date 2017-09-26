import requests

stream = "ice_arena"

def get_stream_data():
    
    url = "https://drdelozier.pythonanywhere.com/stream/query/"
    payload = {
        'time': 'time',
        'place': 'place',
        'city': 'city',
        'state': 'state',
        'lat': 'lat',
        'lon': 'lon',
        'temp': 'temp',
        'humidity': 'humidity',
        'icetemp' : 'icetemp',
        'light': 'light',
        }
    response = requests.get(url + stream)
    data = response.json()
    data = data['result']
    for key in payload.keys():
        data = [item for item in data if key in item]
    data = [item for item in data if item['place'] == 'ice_arena']
    data = [{'time':item['time'], 'place':item['place'], 'lat':item['lat'], 'lon':item['lon'], 'temp':item['temp'], 'humidity':item['humidity'], 'icetemp':item['icetemp'], 'light':item['light']} for item in data]
    return data

def get_chart_data():
    url = "http://drdelozier.pythonanywhere.com/stream/query/"
    payload = {
        'time' : 0,
        'place': 0,
        'city': 0,
        'state': 0,
        'lat': 0,
        'lon': 0,
        'temp': 0,
        'humidity': 0,
        'light': 0,
    }
    response = requests.get(url + stream)
    data = response.json()
    data = data['result']
    for key in payload.keys():
        data = [item for item in data if key in item]
    weather_data = [item for item in data if item['place'] == 'weather']
    ice_arena_data = [item for item in data if item['place'] == 'ice_arena']
    weather_data = [{'time':item['time'], 'temp':item['temp'], 'humidity':item['humidity'], 'light':item['light']} for item in weather_data]
    ice_arena_data = [{'time':item['time'], 'temp':item['temp'], 'icetemp':item['icetemp'], 'humidity':item['humidity'], 'light':item['light']} for item in ice_arena_data]
    return weather_data, ice_arena_data