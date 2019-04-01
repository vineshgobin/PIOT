import json
import sqlite3
from datetime import datetime, timedelta
 


DB_NAME = "sensehat.db"
DATE_FORMAT = "%Y-%m-%d"
ONE_DAY_DELTA = timedelta(days = 1)

with open('config.json') as f:
    data = json.load(f)

# Main function.
def main():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    with connection:
        cursor = connection.cursor()

        row = cursor.execute("SELECT DATE(MIN(DateTIME)), DATE(MAX(DateTime)) FROM sensehat_data").fetchone()
        startDate = datetime.strptime(row[0], DATE_FORMAT)
        endDate = datetime.strptime(row[1], DATE_FORMAT)

        print("Dates:")
        date = startDate
        while date <= endDate:
            row = cursor.execute(
                """SELECT MIN(Temp), MAX(Temp), MIN(Humidity), MAX(Humidity) FROM sensehat_data
                WHERE DateTime >= DATE(:date) AND DateTime < DATE(:date, '+1 day')""",
                { "date": date.strftime(DATE_FORMAT) }).fetchone()
        
        
            minTemp = row[0]
            maxTemp = row[0]
            minHum = row[1]
            maxHum = row[1]

            configMinTemp = data["min_temperature"]
            configMaxTemp = data["max_temperature"]
            configMinHum = data["min_humidity"]
            configMaxHum = data["max_humidity"]

            message = "OK"
            if(minTemp < configMinTemp):
                message = "BAD: below minimum temp" + minTemp
            if(maxTemp > configMinTemp):
                message = "BAD: above maximum temp" + maxTemp
            if(minHum < configMinHum):
                message = "BAD: below minimum humidity" +minHum
            if(maxHum > configMaxHum):
                message = "BAD: above maximum humidity" + maxHum
            else:
                message 
            
            #a = int(requests.form['maxHum - configMaxHum'])
            
            print(date.strftime(DATE_FORMAT) + " | " + message)
           
            date += ONE_DAY_DELTA
    connection.close()

# Execute program.
if __name__ == "__main__":
    main()
