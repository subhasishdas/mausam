#include "dht.h"
#define dht_apin A0 // Analog Pin sensor is connected to
#define carbon_pin A2

#include <SFE_BMP180.h>
#include <Wire.h>
SFE_BMP180 pressure;

dht DHT;
 
void setup(){
 
  Serial.begin(9600);
  delay(500);
  delay(1000);
 pinMode(carbon_pin,INPUT);
  if (pressure.begin())
    Serial.println("BMP180 init success");
  else
  {
    Serial.println("BMP180 init fail\n\n");
    while(1); // Pause forever.
  }
 
}
 
void loop(){
 
    DHT.read11(dht_apin);
    Serial.print("$");
    Serial.print(DHT.humidity,3);
    Serial.print("$");
    Serial.print(DHT.temperature,3);
    Serial.print("$");

 int analogSensor = analogRead(carbon_pin)*3;
    float sensorValue;
 
    //sensorValue = 3*analogRead(A1);
    //Serial.print(sensorValue,3);
    Serial.print(analogSensor);
    Serial.print("$");
    char status;
  double T,P,p0,a;
      status = pressure.startPressure(3);
      if (status != 0)
      {
       delay(status);
        status = pressure.getPressure(P,T);
        if (status != 0)
        {         
          Serial.print(P*0.0295333727,2);
          Serial.println("$");
        }
        else Serial.println("error retrieving pressure measurement\n");
      }
      else Serial.println("error starting pressure measurement\n");
 // delay(5000);  // Pause for 5 seconds.
    delay(1000);
 
}
