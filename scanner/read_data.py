import serial

from .config import DATA_FILEPATH

arduinoComPort = "/dev/ttyACM0"

baudRate = 9600

serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)


def run():
    while True:
        lineOfData = serialPort.readline().decode()
        if len(lineOfData) == 3:
            data = lineOfData.split(",")
            clean_data = [int(d) for d in data]
            print(clean_data)
            coords = calc_coords(*clean_data)
            with open(DATA_FILEPATH, "a") as f:
                f.write(coords)


def calc_coords(distance, pan, tilt):
    """
    Returns string in format X,Y,Z
    """
    # TODO
    pass
