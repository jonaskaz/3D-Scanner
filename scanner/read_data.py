import serial
import math

#Import global variables, including file location for data from serial monitor and
#angle value where pan and tilt are zero for conversion from spherical to cartesian coords.
from config import DATA_FILEPATH, ZERO_TILT_DEGREES, ZERO_PAN_DEGREES

arduinoComPort = "/dev/ttyACM0"

baudRate = 9600

serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)


def run():
    while True:
        lineOfData = serialPort.readline().decode("utf8")  #Read data from serial port
        data = lineOfData.split(",")
        if len(data) == 3:  #If 3 data points are detected, clean and store data
            clean_data = [int(d) for d in data]
            print(clean_data)
            coords = calc_coords(*clean_data)
            with open(DATA_FILEPATH, "a") as f:  #Send data to text file
                f.write(coords)

def convert_raw_reading(raw_reading):
    return 7605*(raw_reading**-0.868)

def calibrate_pan_tilt(pan, tilt):
    pan = math.radians(ZERO_PAN_DEGREES-pan)
    tilt = math.radians(ZERO_TILT_DEGREES-tilt)
    return pan, tilt

#Convert from spherical to cartesian coordinates (sensor gives distance from sensor to each point on letter,
#not distances in x, y, and z directions)
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
