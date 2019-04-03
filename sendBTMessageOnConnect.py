import bluetooth
import time
from temperature import temperature
from humidity import humidity
from pushbulletMessage import pushbulletMessage
from subprocess import check_output

class sendBTMessageOnConnect:
    def main():
        blueConn = bluetooth
        nearby_devices = blueConn.discover_devices()
        pushbullet = pushbulletMessage()

        temp = temperature().getTemp()
        humid = humidity().getHumid()

        message = "Temperature is " + str(temp) + "*C and Humidity is " + str(humid) + "%"

        p = str(check_output(["bt-device", "--list"]))
        start = p.find("(")
        end = p .find(")")
        macAdd = p[start+1:end]

        while (True):
            for macAddresses in nearby_devices:
                if macAdd == macAddresses:
                    print ("Found target bluetooth device!")
                    pushbullet.push_note("Raspberry Pi", message)
                    print("Message sent. \nNext message will be sent in an hour from now IF the bluetooth device is still discoverable.")
                    time.sleep(3600)
                else:
                    print ("Could not find target bluetooth device nearby. Make sure device is discoverable.")

sendBTMessageOnConnect.main()