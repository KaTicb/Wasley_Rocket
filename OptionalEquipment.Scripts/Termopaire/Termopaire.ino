#include <GyverMAX6675.h>

#define SO_PIN 12
#define SCK_PIN 13
#define CS_PIN 10

GyverMAX6675<SCK_PIN, SO_PIN, CS_PIN> termocouple;

void setup(){
  Serial.begin(9600);
}

void loop(){
  static uint32_t timer = millis();
  if(millis() - timer >= 1000){
      timer = millis();
      if(termocouple.readTemp()){
        float T = termocouple.getTemp();
        Serial.println(T);
      }
  }
}