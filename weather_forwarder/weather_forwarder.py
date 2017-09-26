import serial,time
import requests

DELAY = 15

arduino = serial.Serial('COM4', 9600, timeout=2.0)

def get_value(arduino, value):
    text = "[" + value + "]\n"
    bytes = text.encode("latin-1")
    print("Writing " + text)
    arduino.write(bytes)
    while True:
        bytes = arduino.readline() 
        text = bytes.decode("utf-8").strip()
        if text != "?":
            text = text.replace("[","")
            text = text.replace("]","")
            text = text.replace(value,"")
            text = text.replace("=","")
            return float(text)

def post_to_stream(stream, place, city, state, lat, lon, temp, humidity, light):
    url = "http://drdelozier.pythonanywhere.com/stream/store/"
    payload = {
        'place': str(place),
        'city': str(city),
        'state': str(state),
        'lat': str(lat),
        'lon': str(lon),
        'temp': str(temp),
        'humidity': str(humidity),
        'light': str(light),
    }
    response = requests.get(url + stream, params=payload)
    print(response.status_code)
    print(response.url)
    print(response.text)

time.sleep(3)
clock = time.time()
while True:
    temp = get_value(arduino,"TEMP")
    humidity = get_value(arduino,"HUMIDITY")
    light = get_value(arduino, "A0")
    print(temp, humidity)
    temp = round((temp * 1.8) + 32, 1)
    post_to_stream("ice_arena", "weather", "kent", "OH", 41.145734, -81.336070, temp, humidity, light)
    while time.time() < clock + DELAY:
        time.sleep(0.5)
    clock = clock + DELAY 



            
