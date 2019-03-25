from __future__ import print_function
from temperature import *
from humidity import *
import json

##open json file and get data
with open('config.json') as f:
    data = json.load(f)

class monitorAndNotify:

    def temperature(self):

        # Temperature right now
        temp = round(temperature().getTemp())
        print("Temperature is " + str(temp) + " *C.")

        # Maximum and minimum temperatures
        max_temp = data["max_temperature"]
        min_temp = data["min_temperature"]

        # Comparing current temperature to min and max
        if temp > max_temp:
            result = (str(temp - max_temp) + " *C above maximum temperature.")
        if temp < min_temp:
            result = (str(min_temp - temp) + " *C under minimum temperature.")
        if (temp < max_temp) and (temp > min_temp):
            result = ("Temperature is within range.")

        return result

    def humidity(self):

        # Humidity right now
        humid = round(humidity().getHumid())
        print("Humidity is " + str(humid) + "%.")

        # Maximum and minimum humidities
        max_humid = data["max_humidity"]
        min_humid = data["min_humidity"]

        # Comparing current humidity to min and max
        if humid > max_humid:
            result = (str(humid - max_humid) + "% above maximum humidity.")
        if humid < min_humid:
            result = (str(min_humid - humid) + "% under minimum humidity.")
        if (humid < max_humid) and (humid > min_humid):
            result = ("Humidity is within range.")

        return result



