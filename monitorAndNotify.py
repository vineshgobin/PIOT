# monitorAndNotify.py

from sense_hat import SenseHat
from sense_hat import SenseHat
import json

with open('config.json') as f:
    data = json.load(f)

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
print("Temperature")

print(temp)
##max temp
a = " Degrees Above Max Temp"
x = data["max_temperature"]
y = temp - x
y = round(y)
y = str(y)

##min temp
b = " Degrees Below Min Temp"
i = data["min_temperature"]
z = i - temp
z = round(z)
z = str(z)


if temp > data["max_temperature"]:
    
    print(y + a )

if temp < data["min_temperature"]:
    print(z + b)

if temp > data["min_temperature"] and temp < data["max_temperature"] :
    print("Within Range")


print("-----------------------")

sense = SenseHat()
sense.clear()

humidity = sense.get_humidity()
print("Humidity")
print(humidity)

##min humidity
e = "% below min Humidity"
k = data["min_humidity"]
hum1 = ((humidity - k)/k) * 100
hum1 = round(hum1)
hum1  = str(hum1)

##min humidity
c = "% below min Humidity"
j = data["min_humidity"]
hum = ((j - humidity)/j) * 100
hum = round(hum)
hum  = str(hum)


if temp > data["max_humidity"]:
    print(hum1 + e)

if temp < data["min_humidity"]:
     print(hum + c)

if temp > data["min_humidity"] and temp < data["max_humidity"] :
    print("Within Range")
