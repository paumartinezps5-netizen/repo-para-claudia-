int pinLED=10;
int polsador=2;
int estat=LOW;

void setup() {
  pinMode(pinLED, OUTPUT);
  pinMode(polsador, INPUT);
}

void loop() {
  if (digitalRead(polsador)==HIGH) {
    if (estat==LOW) {
      estat=HIGH;
    } else {
      estat=LOW;
    }
    digitalWrite(pinLED, estat);
    delay(50);
    while (digitalRead(polsador)==HIGH) {
    }
    delay(50);
  }
}
