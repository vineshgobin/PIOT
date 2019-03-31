import bluetooth
from temperature import temperature
from humidity import humidity
from pushbulletMessage import pushbulletMessage

class sendBTMessageOnConnect:
    def main():

        # Vinesh Gobin's phone
        target_name = "OnePlus 5T"
        target_address = None

        blueConn = bluetooth
        nearby_devices = blueConn.discover_devices()
        pushbullet = pushbulletMessage()

        temp = temperature().getTemp()
        humid = humidity().getHumid()

        message = "Temperature is " + str(temp) + "*C and Humidity is " + str(humid) + "%"

        while (True):
            for bdaddr in nearby_devices:
                if target_name == blueConn.lookup_name( bdaddr ):
                    target_address = bdaddr
                    break

            if target_address is not None:
                print ("Found target bluetooth device!")
                pushbullet.push_note("Raspberry Pi", message)
                print("Message sent. Next message will be sent in an hour from now IF the bluetooth device is still discoverable.")
                time.sleep(3600)
            else:
                print ("Could not find target bluetooth device nearby. Make sure device is discoverable.")

sendBTMessageOnConnect.main()