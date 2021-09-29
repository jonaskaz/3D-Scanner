#include <Servo.h>

Servo panServo;
Servo tiltServo;

int startPan = 80;
int panPos = startPan;
int startTilt = 35;
int endPan = 30;
int endTilt = 65;
int panStep = 1;
int tiltStep = 1;
int tiltDelay = 20;
int panDelay = 20;
int sensorPin = A0;

void setServoInit() {
  // Set servo initial positions
  panServo.write(startPan);
  delay(1000);
  tiltServo.write(startTilt);
  delay(3000);
}

void setup() {
  panServo.attach(10);
  tiltServo.attach(9);
  Serial.begin(9600);
  setServoInit();
}

float getReading() {
  // Get 5 sensor readings and return their average
  float rawRead1 = analogRead(sensorPin);
  float rawRead2 = analogRead(sensorPin);
  float rawRead3 = analogRead(sensorPin);
  float rawRead4 = analogRead(sensorPin);
  float rawRead5 = analogRead(sensorPin);
  return (rawRead1 + rawRead2 + rawRead3 + rawRead4 + rawRead5)/5;
}


void sendReadings(int reading, int pan, int tilt) {
  // Send a sensor reading with pan and tilt over serial
  Serial.print(reading);    Serial.print(",");
  Serial.print(pan);        Serial.print(",");
  Serial.println(tilt);
}

void tiltUp() {
  // Tilt sensor up, sending sensor readings at each position
  for (int pos=startTilt; pos<= startTilt + endTilt; pos+=tiltStep) {
      tiltServo.write(pos);
      delay(tiltDelay);
      sendReadings(getReading(), panPos, pos);
    }
}

void tiltDown() {
  // Tilt sensor down, sending sensor readings at each position
  for (int pos=startTilt + endTilt; pos>= startTilt; pos-=tiltStep) {
      tiltServo.write(pos);
      delay(tiltDelay);
      sendReadings(getReading(), panPos, pos);
    }
}

void loop() {
  while (panPos - 2*panStep >= endPan) {
    // Pan the sensor while tilting up and down
    tiltUp();
//    panPos-=panStep;
//    panServo.write(panPos);
//    delay(panDelay);
//    tiltDown();
//    panPos-=panStep;
//    panServo.write(panPos);
//    delay(panDelay);
//  }
//  panPos = startPan;
//  setServoInit();
  delay(5000);
}
