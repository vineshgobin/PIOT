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

        noMsgSent = True

        temp = temperature().getTemp()
        humid = humidity().getHumid()

        message = "Temperature is: " + str(temp) + "*C and Humidity is " + str(humid) + "%"

        while (noMsgSent):
            for bdaddr in nearby_devices:
                if target_name == blueConn.lookup_name( bdaddr ):
                    target_address = bdaddr
                    break

            if target_address is not None:
                print ("Found target bluetooth device!")
                pushbullet.push_note("Raspberry Pi", message)
                print("Message sent, no further messages will be sent until reconnected.")
                noMsgSent = False
            else:
                print ("Could not find target bluetooth device nearby.")

sendBTMessageOnConnect.main()