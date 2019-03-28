from sense_hat import SenseHat

sense = SenseHat()

class humidity:

    def getHumid(self):
        sense.clear()
        return round(sense.get_humidity(), 2)