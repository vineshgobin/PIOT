from monitorAndNotify import *
from pushbulletMessage import pushbulletMessage
import datetime
import json
import time
import os

##open json file and get data
with open('config.json') as f:
    data = json.load(f)

class main:

    # prints time, temperature and humidity for debugging purposes
    def sendMessage(self, currentTemp, min_temp, max_temp, currentHumid, min_humid, max_humid, today, pushbullet, file):
        if (currentTemp < min_temp):
            pushbullet.push_note("Raspberry Pi", "WARNING: Temperature is less than minimum. (%0.2f*C)" % currentTemp)
        if (currentTemp > max_temp):
            pushbullet.push_note("Raspberry Pi", "WARNING: Temperature is more than maximum. (%0.2f*C)" % currentTemp)
        if (currentHumid < min_humid):
            pushbullet.push_note("Raspberry Pi", "WARNING: Humidity is less than minimum. (%0.2f)" % currentHumid)
        if (currentTemp > max_humid):
            pushbullet.push_note("Raspberry Pi", "WARNING: Humidity is more than maximum. (%0.2f)" % currentHumid)
        file.write(today + "\n")

    def main():

        #dateAndTime
        now = datetime.datetime.now()
        today = now.strftime("%y%m%d")

        #Pushbullet
        pushbullet = pushbulletMessage()

        # Maximum and minimum temperatures
        max_temp = data["max_temperature"]
        min_temp = data["min_temperature"]

        # Maximum and minimum humidities
        max_humid = data["max_humidity"]
        min_humid = data["min_humidity"]

        currentTemp = temperature().getTemp()
        currentHumid = humidity().getHumid()
        while (currentHumid == 0):
            currentHumid = humidity().getHumid()

        


        # Gets temperature and humidity
        temp = monitorAndNotify().temperature()
        
        humid = monitorAndNotify().humidity()
        

        # Creates a new database if not already created
        db_exists = os.path.isfile('/home/pi/IOT-A1/sensehat.db')

        if (not db_exists):
            monitorAndNotify().initDB()

        monitorAndNotify().datab(now.strftime("%Y-%m-%d"),currentTemp, currentHumid)

        # Creates a text file where the last date when a notification was sent is recorded.
        file_exists = os.path.isfile('/home/pi/IOT-A1/dayTracker.txt')

        if (not file_exists):
            file = open ("/home/pi/IOT-A1/dayTracker.txt", "w")
            main().sendMessage(currentTemp, min_temp, max_temp, currentHumid, min_humid, max_humid, today, pushbullet, file)
            file.close()

        # Compares today's date with the date in the file. If the date changed, a new notification is sent to the user when the conditions are met.
        file = open ("/home/pi/IOT-A1/dayTracker.txt", "r+")
        lastDate = file.read().splitlines()[-1]
        if (today > lastDate):
            main().sendMessage(currentTemp, min_temp, max_temp, currentHumid, min_humid, max_humid, today, pushbullet, file)
        file.close()

main.main()