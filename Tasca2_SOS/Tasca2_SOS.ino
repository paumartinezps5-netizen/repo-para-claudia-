int pinLED=10;
int polsador=2;
int punt=200;
int ratlla=600;
int pausaLletra=400;
int pausaMissatge=1200;

void setup() {
  pinMode(pinLED, OUTPUT);
  pinMode(polsador, INPUT);
}

void loop() {
  if (digitalRead(polsador)==HIGH) {
    digitalWrite(pinLED, HIGH);
    delay(punt);
    digitalWrite(pinLED, LOW);
    delay(punt);
    digitalWrite(pinLED, HIGH);
    delay(punt);
    digitalWrite(pinLED, LOW);
    delay(punt);
    digitalWrite(pinLED, HIGH);
    delay(punt);
    digitalWrite(pinLED, LOW);
    delay(punt);
    delay(pausaLletra);
    digitalWrite(pinLED, HIGH);
    delay(ratlla);
    digitalWrite(pinLED, LOW);
    delay(punt);
    digitalWrite(pinLED, HIGH);
    delay(ratlla);
    digitalWrite(pinLED, LOW);
    delay(punt);
    digitalWrite(pinLED, HIGH);
    delay(ratlla);
    digitalWrite(pinLED, LOW);
    delay(punt);
    delay(pausaLletra);
    digitalWrite(pinLED, HIGH);
    delay(punt);
    digitalWrite(pinLED, LOW);
    delay(punt);
    digitalWrite(pinLED, HIGH);
    delay(punt);
    digitalWrite(pinLED, LOW);
    delay(punt);
    digitalWrite(pinLED, HIGH);
    delay(punt);
    digitalWrite(pinLED, LOW);
    delay(punt);
    delay(pausaMissatge);
  }
}
