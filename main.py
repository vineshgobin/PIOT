from monitorAndNotify import *
import datetime

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


main.main()