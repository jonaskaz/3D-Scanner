import serial

from config import DATA_FILEPATH

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


def calc_coords(distance, pan, tilt):
    """
    Returns string in format X,Y,Z
    """
    # TODO
    return str(distance) + "," + str(pan) + "," + str(tilt) + "\n"

if __name__ == "__main__":
    run()
