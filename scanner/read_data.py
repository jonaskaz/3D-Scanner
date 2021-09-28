import serial  #Import relevant libraries
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

def convert_raw_reading(raw_reading):  #Using curve from calibration, convert raw reading to actual distance
    return 174-0.568*raw_reading + 5.24e-4 * raw_reading**2

def calibrate_pan_tilt(pan, tilt):  #Calibrates angles sent from serial monitor to our x, y, and z axes
    pan = ZERO_PAN_DEGREES-pan
    tilt = ZERO_TILT_DEGREES-tilt
    return pan, tilt  #Angles we can use in conversion from spherical to cartesian coordinates

#Convert from spherical to cartesian coordinates (sensor gives distance from sensor to each point on letter,
#not distances in x, y, and z directions)
def calc_coords(raw_reading, pan, tilt):  
    """
    Returns string in format X,Y,Z
    """
    distance = convert_raw_reading(raw_reading)
    pan, tilt = calibrate_pan_tilt(pan, tilt)
    z = math.cos(math.radians(tilt)) * distance
    r = math.sin(math.radians(tilt)) * distance
    y = math.sin(math.radians(pan)) * r
    x = math.cos(math.radians(pan)) * r
    return str(x) + "," + str(y) + "," + str(z) + "\n"

if __name__ == "__main__":
    run()
