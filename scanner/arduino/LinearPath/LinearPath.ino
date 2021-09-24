#include <Servo.h>

Servo panServo;
Servo tiltServo;

int startPan = 72;
int panPos = startPan;
int startTilt = 25;
int endPan = 120;
int endTilt = 90;
int panStep = 5;
int tiltStep = 1;
int tiltDelay = 20;
int panDelay = 50;
int sensorPin = A0;

void setServoInit() {
  panServo.write(startPan);
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
  float rawRead = analogRead(sensorPin);
  return int(174 - 0.568*rawRead + (5.24*pow(10, -4)) * pow(rawRead, 2));
}


void sendReadings(int reading, int pan, int tilt) {
  Serial.print(reading);    Serial.print(",");
  Serial.print(pan);        Serial.print(",");
  Serial.println(tilt);
}

void tiltUp() {
  for (int pos=startTilt; pos<= startTilt + endTilt; pos+=tiltStep) {
      tiltServo.write(pos);
      delay(tiltDelay);
      sendReadings(getReading(), panPos, pos);
    }
}

void tiltDown() {
  for (int pos=startTilt + endTilt; pos>= startTilt; pos-=tiltStep) {
      tiltServo.write(pos);
      delay(tiltDelay);
      sendReadings(getReading(), panPos, pos);
    }
}

void loop() {
  while (panPos + 2*panStep <= endPan) {
    tiltUp();
    panPos+=panStep;
    panServo.write(panPos);
    delay(panDelay);
    tiltDown();
    panPos+=panStep;
    panServo.write(panPos);
    delay(panDelay);
  }
  panPos = startPan;
  setServoInit();
  delay(5000);
}
