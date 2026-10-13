int pinLED=10;
int boto=2;
int punt=200;
int ratlla=600;
int pausaLletra=400;
int pausaMissatge=1200;
int n=0;

void setup() {
  pinMode(pinLED, OUTPUT);
  pinMode(boto, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(boto)==LOW) {
    for (n=0; n<3; n++) {
      digitalWrite(pinLED, HIGH);
      delay(punt);
      digitalWrite(pinLED, LOW);
      delay(punt);
    }
    delay(pausaLletra);
    for (n=0; n<3; n++) {
      digitalWrite(pinLED, HIGH);
      delay(ratlla);
      digitalWrite(pinLED, LOW);
      delay(punt);
    }
    delay(pausaLletra);
    for (n=0; n<3; n++) {
      digitalWrite(pinLED, HIGH);
      delay(punt);
      digitalWrite(pinLED, LOW);
      delay(punt);
    }
    delay(pausaMissatge);
  }
}
