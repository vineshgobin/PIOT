import sqlite3
from datetime import datetime, timedelta
import json, csv

DB_NAME = "sensehat.db"
DATE_FORMAT = "%y%m%d"
ONE_DAY_DELTA = timedelta(days = 1)

with open('config.json') as f:
    data = json.load(f)


def report():

    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    with connection:
        cursor = connection.cursor()

        row = cursor.execute("SELECT DATE(MIN(DateTime)), DATE(MAX(DateTime)) FROM SENSEHAT_data").fetchone()
        startDate = datetime.strptime(row[0], DATE_FORMAT)
        endDate = datetime.strptime(row[1], DATE_FORMAT)

        print("Dates:")
        date = startDate
        while date <= endDate:
            row = cursor.execute(
                """SELECT MIN(Temp),MAX(Temp) FROM SENSEHAT_data
                WHERE DateTime >= DATE(:date) AND DateTime < DATE(:date, '+1 day')""",
                { "date": date.strftime(DATE_FORMAT) }).fetchone()

            minTemp = row[0]
            maxTemp = row[1]
            configMinTemp = data["min_temperature"]
            configMaxTemp = data["max_temperature"]

            message = "OK" 

            if(float(minTemp) < configMinTemp):
                message = "BAD: below minimum temp" + str(minTemp)
            if(float(maxTemp) > configMaxTemp):
                message = "BAD: above max temp" + str(maxTemp)
            
            print(date.strftime(DATE_FORMAT) + " | " + message)

                
            row = cursor.execute(
                """SELECT MIN(Humidity),MAX(Humidity) FROM SENSEHAT_data
                WHERE DateTime >= DATE(:date) AND DateTime < DATE(:date, '+1 day')""",
                { "date": date.strftime(DATE_FORMAT) }).fetchone()

            
            minHum = row[0]
            maxHum = row[1]
            configMinHum = data["min_humidity"]
            configMaxHum = data["max_humidity"]
             
           
            msg = "OK" 
            
            if(float(minHum) < configMinHum):
                msg = "BAD: below minimum humidity" + str(minHum)
            
            if(float(maxHum) < configMaxHum):
                msg = "BAD: above max humidity" + str(maxHum)
            else:
                msg
            
            print(date.strftime(DATE_FORMAT) + " | " + msg)
            
            date += ONE_DAY_DELTA

        
        myData = [[date.strftime(DATE_FORMAT),message],[date.strftime(DATE_FORMAT),msg]]

        csv.register_dialect('myDialect', delimiter='|', quoting=csv.QUOTE_NONE)

        myFile = open('report.csv', 'w')  
        
        with myFile:  
            writer = csv.writer(myFile, dialect='myDialect')
            writer.writerows(myData)
           

    connection.close()

if __name__ == "__main__":
    report()

    


