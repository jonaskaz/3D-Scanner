
#include <Servo.h>

Servo panServo;
Servo tiltServo;

int pos = 0;
int pan = 30;  //pan servo angle value
int tilt = 0;  //tilt servo angle value
int panDegrees = 180;
int servoStep = 5;
int servoDelay = 150;
int sensorPin = A0;

void setup() {
  panServo.attach(10);
  tiltServo.attach(9);
  Serial.begin(9600);
  panServo.write(0);
  delay(3000);

}

float getReading() {
  float rawRead = analogRead(sensorPin);
  return 174 - (0.568 * rawRead) + ((5.24 * pow(10, -4)) * pow(rawRead, 2));
}

void loop() {
//  for (pos = 0; pos <= panDegrees; pos += servoStep) {
//    //Serial.println(analogRead(sensorPin));
//    Serial.println(getReading());
//    panServo.write(pos);
//    tiltServo.write(pos);
//    delay(servoDelay);
//  }
//  for (pos = panDegrees; pos >= 0; pos -= servoStep) {
//    //Serial.println(analogRead(sensorPin));
//    panServo.write(pos);
//    tiltServo.write(pos);
//    Serial.println(getReading());
//    delay(servoDelay);
//  }

  int count = 0;
  int stepcount = 0;
  int numsteps = 15;
  int tiltstep = 90;
  int panstep = 15;

while(pan < 150){  //Stop loop once pan angle has reached 150
  //for (count =0; count < 2; count++) {
    if (tilt == 0) {  //Check if starting tilt angle is 0
      while (tilt < 90) {  //Run it until the tilt angle reaches 90
        tilt = tilt + (tiltstep / numsteps);  //change tilt angle by (final-initial)/number of steps we want to take
        pan = pan + (panstep / numsteps);  //same but for pan angle

        panServo.write(pan);  //Move the servo to angle
        tiltServo.write(tilt);
        delay(servoDelay);
        Serial.print("Pan: ");
        Serial.print(pan);
        Serial.print(", Tilt: ");
        Serial.println(tilt);
        //Serial.print(", Step Count: ");
        //Serial.println(stepcount);
        //stepcount ++;
        //  for (tilt = 0; tilt <= 90; tilt += servoStep && pan +=) {
        //}
      }
    }
    else if (tilt == 90) {  //Check if starting tilt angle is 90
      while (tilt > 0) {  //Run until the tilt angle reaches 0
        tilt = tilt - (tiltstep / numsteps);
        pan = pan + (panstep / numsteps);

        panServo.write(pan);
        tiltServo.write(tilt);
        delay(servoDelay);
        Serial.print("Pan: ");
        Serial.print(pan);
        Serial.print(", Tilt: ");
        Serial.println(tilt);
        //Serial.print(", Step Count: ");
        //Serial.println(stepcount);
        //stepcount++;
      }
    }
    delay(500);
    //stepcount = 0;
    //count ++;

    //Serial.print("Step Count: ");
    //Serial.print(stepcount);
    //Serial.print("Count: ");
    //Serial.println(count);
  }
  //    else if tilt == 90{
  //
  //    }
}
