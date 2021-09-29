import serial
import math

from config import DATA_FILEPATH, ZERO_TILT_DEGREES, ZERO_PAN_DEGREES

arduinoComPort = "/dev/ttyACM0"

baudRate = 9600

serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)


def run():
    while True:
        lineOfData = serialPort.readline().decode("utf8")
        data = lineOfData.split(",")
        if len(data) == 3:
            clean_data = [int(d) for d in data]
            print(clean_data)
            coords = calc_coords(*clean_data)
            with open(DATA_FILEPATH, "a") as f:
                f.write(coords)

def convert_raw_reading(raw_reading):
    return 7605*(raw_reading**-0.868)

def calibrate_pan_tilt(pan, tilt):
    pan = math.radians(ZERO_PAN_DEGREES-pan)
    tilt = math.radians(ZERO_TILT_DEGREES-tilt)
    return pan, tilt

def calc_coords(raw_reading, pan, tilt):
    """
    Returns string in format X,Y,Z
    """
    distance = convert_raw_reading(raw_reading)
    pan, tilt = calibrate_pan_tilt(pan, tilt)
    z = math.cos(tilt) * distance
    r = math.sin(tilt) * distance
    y = math.sin(pan) * r
    x = math.cos(pan) * r
    return str(x) + "," + str(y) + "," + str(z) + "\n"

if __name__ == "__main__":
    run()
