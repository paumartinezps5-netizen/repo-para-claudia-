int pinLED=10;
int polsador=2;

void setup() {
  pinMode(pinLED, OUTPUT);
  pinMode(polsador, INPUT);
}

void loop() {
  if (digitalRead(polsador)==HIGH) {
    if (digitalRead(pinLED)==LOW) {
      digitalWrite(pinLED, HIGH);
    } else {
      digitalWrite(pinLED, LOW);
    }
    delay(500);
  }
}
