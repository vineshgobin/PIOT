from sense_hat import SenseHat

sense = SenseHat()

class temperature:

    def getTemp(self):
        sense.clear()
        return round(sense.get_temperature(), 2)