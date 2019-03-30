import csv
import sqlite3
from os import path

class createReport:

    def report():

        # Connects to database
        conn = sqlite3.connect('/home/pi/IOT-A1/sensehat.db')
        cursor = conn.cursor()
        cursor.execute("SELECT DateTime,Temp,Humidity FROM SENSEHAT_data WHERE (Temp < 20 OR Temp > 30) AND (Humidity < 50 OR Humidity > 60)")
        

        # Writes report
        with open("report.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, quoting = csv.QUOTE_MINIMAL)
            #csv_writer.writerow([i[0] for i in cursor.description]) # write headers
            csv_writer.writerow(["Date: Status"])
            csv_writer.writerows(cursor)

createReport.report()