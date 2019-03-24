from sense_hat import SenseHat

sense = SenseHat()

class humidity:

    def getHumid(self):
        sense.clear()
        return sense.get_humidity()