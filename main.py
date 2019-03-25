from monitorAndNotify import *
import datetime
import sqlite3
dbname = 'sensehat.db'
##sampleFreq = 1 # time in seconds

class main:

    # prints time, temperature and humidity for debugging purposes
    def main():

        #dateAndTime
        now = datetime.datetime.now()
        print ("Current date and time :" , end = ' ')
        print (now.strftime("%d-%m-%y %H:%M:%S"))
        print()

        temp = monitorAndNotify().temperature()
        print(temp)
        print()
        print("-"*16)
        print()
        humid = monitorAndNotify().humidity()
        print(humid)

con = lite.connect('sensehat.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS SENSEHAT_data")
    cur.execute("CREATE TABLE SENSEHAT_data(timestamp DATETIME, temp NUMERIC, humidity NUMERIC)")


    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'), (?))", (temp,) (humid,))
    conn.commit()
    conn.close()
        
    def displayData():
            conn=sqlite3.connect(dbname)
            curs=conn.cursor()
            print ("\nEntire database contents:\n")
            for row in curs.execute("SELECT * FROM SenseHat_data"):
                print (row)
            conn.close()


# Execute program 
displayData()

main.main()