import csv
import sqlite3
from os import path

class createReport:

    def report():

        # Connects to database
        conn = sqlite3.connect('/home/pi/IOT-A1/sensehat.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM SENSEHAT_data WHERE Humidity > 0;")

        # Writes report
        with open("/home/pi/IOT-A1/report.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([i[0] for i in cursor.description]) # write headers
            csv_writer.writerows(cursor)

createReport.report()