from __future__ import print_function
from pushbulletMessage import pushbulletMessage
from temperature import temperature
from humidity import humidity
import json
import sqlite3
dbname = '/home/pi/IOT-A1/sensehat.db'

##open json file and get data
with open('config.json') as f:
    data = json.load(f)

class monitorAndNotify:

    def temperature(self):

        # Temperature right now
        temp = round(temperature().getTemp(), 2)

        # Maximum and minimum temperatures
        max_temp = data["max_temperature"]
        min_temp = data["min_temperature"]

        # Comparing current temperature to min and max
        if temp > max_temp:
            result = ("Bad: "+ str(temp - max_temp) + "*C above maximum temperature.")
        if temp < min_temp:
            result = ("Bad: "+ str(min_temp - temp) + "*C under minimum temperature.")
        if (temp < max_temp) and (temp > min_temp):
            result = ("OK.")

        return result

    def humidity(self):

        # Humidity right now
        humid = round(humidity().getHumid(), 2)
        while (humid == 0):
            humid = round(humidity().getHumid(), 2)

        # Maximum and minimum humidities
        max_humid = data["max_humidity"]
        min_humid = data["min_humidity"]

        # Comparing current humidity to min and max
        if humid > max_humid:
            result = ("Bad: "+ str(humid - max_humid) + "% above maximum humidity.")
        if humid < min_humid:
            result = ("Bad: "+ str(min_humid - humid) + "% under minimum humidity.")
        if (humid < max_humid) and (humid > min_humid):
            result = ("OK.")

        return result

    def initDB(self):
        con = sqlite3.connect(dbname)
        cur = con.cursor() 
        cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
        cur.execute("CREATE TABLE SENSEHAT_data(TimeStamp DATETIME,Temp DOUBLE,Humidity DOUBLE)")

    def datab(self, now, temp, humidity):
        conn=sqlite3.connect(dbname)
        curs=conn.cursor()
        curs.execute('''INSERT INTO SENSEHAT_data (TimeStamp,Temp, Humidity) VALUES (?,?,?)''', (now, temp, humidity,))
        conn.commit()
        conn.close()



