import serial, time, requests, random
from random import randint
from twilio.rest import Client
DELAY = 15.0
GEO_LIST = {'41.145585':'-81.336266', '41.145423':'-81.336183', '41.145799':'-81.335671', '41.145605':'-81.335569', '41.145550':'-81.336071', '41.145673':'-81.335749', '41.145600':'-81.335907'}
post_stream = "ice_arena2"
arduino = serial.Serial('COM5', 9600, timeout=2.0)

# Your Account SID from twilio.com/console
account_sid = "AC4e30ebe23a2b99d90ecc1449a843204b"
# Your Auth Token from twilio.com/console
auth_token  = "416ae3af93ab828cf55b4fb61b0b44c7"

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

def send_msg(temp, humidity, icetemp):
    client = Client(account_sid, auth_token)
    msg = 'Temp=' + str(temp) +' Humidity=' + str(humidity) + ' Ice Temp=' + str(icetemp)
    message = client.messages.create(
        to="7736736732", 
        from_="+17736739767",
        body=msg)
    print(message.sid)

def post_to_stream(stream, place, city, state, lat, lon, temp, humidity, icetemp, light):
    url = "http://drdelozier.pythonanywhere.com/stream/store/"
    payload = {
        'place': str(place),
        'city': str(city),
        'state': str(state),
        'lat': str(lat),
        'lon': str(lon),
        'temp': str(temp),
        'humidity': str(humidity),
        'icetemp': str(icetemp),
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
   icetemp = get_value(arduino,"ICETEMP")
   light = get_value(arduino,"A0")
   latitude, longitude = random.choice(list(GEO_LIST.items()))
   #temp = random.randint(48, 60)
   #humidity = random.randint(43, 50)
   #icetemp = random.randint(16, 22)
   temp = round((temp * 1.8) + 32, 1)
   icetemp = round((icetemp * 1.8) + 32, 1)
   post_to_stream(post_stream,"ice_arena","kent","OH",latitude,longitude,temp,humidity,icetemp,light)
   if(temp < 55 or humidity < 48 or icetemp < 16):
       send_msg(temp, humidity, icetemp)

   if(temp > 60 or humidity > 50 or icetemp > 22):
       send_msg(temp, humidity, icetemp)

   while time.time() < clock + DELAY:
       time.sleep(0.5)
   clock = clock + DELAY