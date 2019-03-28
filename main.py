from monitorAndNotify import *
import datetime
import time
import os

class main:

    # prints time, temperature and humidity for debugging purposes
    def main():

        #dateAndTime
        now = datetime.datetime.now()

        print ("Current date and time :" , end = ' ')
        print (now.strftime("%d-%m-%y %H:%M:%S"))
        print()


        # Prints temperature and humidity
        temp = monitorAndNotify().temperature()
        print(temp)
        print()
        print("-"*16)
        print()
        humid = monitorAndNotify().humidity()
        print(humid)
        print()

        # Creates a new database if not already created
        exists = os.path.isfile('/home/pi/IOT-A1/sensehat.db')

        if (not exists):
            monitorAndNotify().initDB()

        monitorAndNotify().datab(now,temperature().getTemp(), humidity().getHumid())

main.main()