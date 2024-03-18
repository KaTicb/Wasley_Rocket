int ThermistorPin = A0; // Подключите термистор к аналоговому входу A0
float Vo = 0;
float R1 = 10000; // Укажите сопротивление резистора R1
float logR2, R2, T;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07; // Коэффициенты для уравнения Steinhart-Hart

void setup() {
 Serial.begin(9600);
}

void loop() {
 Vo = analogRead(ThermistorPin);
 R2 = R1 * (1023.0 / Vo - 1.0);
 logR2 = log(R2);
 T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
 // T += 273.15; // Преобразование из градусов Цельсия в Кельвины

 Serial.print("Температура: "); 
 Serial.print(Vo);
 Serial.println(" V"); 

 delay(500);
}