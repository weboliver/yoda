import serial

from Sensors.sensor import Sensor


class UltraSonic(Sensor):

    def __init__(self):
        self._serial = serial.Serial ("/dev/ttyS0", 115200)

    def getPort(self):
        return self._serial

    def read_one(self):
        distance = {}
        ser = self.getPort()
        # Waiting Strings verwerfen
        ser.read_all()
        received_data = ser.readline()  #read serial port
        result = str(received_data.decode('utf-8')).split(",")
        # print(result)
        distance[result[0]] = round(float(result[1]))
        distance[result[2]] = round(float(result[3]))
        return distance
