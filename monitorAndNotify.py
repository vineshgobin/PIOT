from __future__ import print_function
from temperature import *
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

        if temp > max_temp:
            result = (str(temp - max_temp) + " *C above maximum temperature.")
        if temp < min_temp:
            result = (str(min_temp - temp) + " *C under minimum temperature.")
        if (temp < max_temp) and (temp > min_temp):
            result = ("Temperature is within range.")

        return result




