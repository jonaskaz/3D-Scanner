import serial

arduinoComPort = "/dev/ttyACM0"

baudRate = 9600

serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)
data = []

while True:
  lineOfData = serialPort.readline().decode()
  if len(lineOfData) == 3:
    for d in lineOfData:
      d = int(d)
    data_list = lineOfData.split(",")
    print(data_list)
    data.append(data_list)
