import sqlite3
from datetime import datetime, timedelta
import json, csv

DB_NAME = "/home/pi/IOT-A1/sensehat.db"
DATE_FORMAT = "%Y-%m-%d"
ONE_DAY_DELTA = timedelta(days = 1)

with open('config.json') as f:
    data = json.load(f)

class createReport:
    def report():

        connection = sqlite3.connect(DB_NAME)
        connection.row_factory = sqlite3.Row
        with connection:
            cursor = connection.cursor()

            row = cursor.execute("SELECT DATE(MIN(TimeStamp)), DATE(MAX(TimeStamp)) FROM SENSEHAT_data").fetchone()
            startDate = datetime.strptime(row[0], DATE_FORMAT)
            endDate = datetime.strptime(row[1], DATE_FORMAT)

            print("Dates:")
            date = startDate
            while date <= endDate:
                row = cursor.execute(
                    """SELECT MIN(Temp),MAX(Temp) FROM SENSEHAT_data
                    WHERE TimeStamp >= DATE(:date) AND TimeStamp < DATE(:date, '+1 day')""",
                    { "date": date.strftime(DATE_FORMAT) }).fetchone()

                minTemp = row[0]
                maxTemp = row[1]
                configMinTemp = data["min_temperature"]
                configMaxTemp = data["max_temperature"]

                msg = "OK"
                message = "BAD:" 

                diff1 = configMinTemp - minTemp
                diff2 = maxTemp - configMaxTemp

                if(float(minTemp) < configMinTemp):
                    message += " " + str(diff1)+ "* below minimum temperature" 
                if(float(maxTemp) > configMaxTemp):
                    message += " " + str(diff2)+ "* above max temperature"
                
                print(date.strftime(DATE_FORMAT) + " | " + message)

                
                
                row = cursor.execute(
                    """SELECT MIN(Humidity),MAX(Humidity) FROM SENSEHAT_data
                    WHERE TimeStamp >= DATE(:date) AND TimeStamp < DATE(:date, '+1 day')""",
                    { "date": date.strftime(DATE_FORMAT) }).fetchone()

                
                minHum = row[0]
                maxHum = row[1]
                configMinHum = data["min_humidity"]
                configMaxHum = data["max_humidity"]

                diff3 = configMinHum - minHum
                diff4 = maxHum - configMaxHum
                
                if(float(minHum) < configMinHum):
                    message += " " + str(diff3)+ " below minimum humidity"
                
                if(float(maxHum) > configMaxHum):
                    message += " " + str(diff4)+ " above max humidity"
                
                print(date.strftime(DATE_FORMAT) + " | " + msg)

                if ((maxTemp < configMaxTemp) and (minTemp > configMinTemp) and (maxHum < configMaxHum) and (minHum > configMinHum)):
                    myData = [[date.strftime(DATE_FORMAT),msg]]
                else:
                    myData = [[date.strftime(DATE_FORMAT),message]]

                # myData = [[date.strftime(DATE_FORMAT),message],[date.strftime(DATE_FORMAT),msg]]
            
                date += ONE_DAY_DELTA
        
            csv.register_dialect('myDialect', delimiter='|', quoting=csv.QUOTE_NONE)

            with open('/home/pi/IOT-A1/report.csv', 'w') as myFile:  
                writer = csv.writer(myFile, dialect='myDialect')
                writer.writerows(myData)
            

        connection.close()

createReport.report()
    


