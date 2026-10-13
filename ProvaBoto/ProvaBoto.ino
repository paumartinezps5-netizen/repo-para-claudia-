int pinLED=10;
int boto=2;

void setup() {
  pinMode(pinLED, OUTPUT);
  pinMode(boto, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  Serial.println(digitalRead(boto));
  if (digitalRead(boto)==LOW) {
    digitalWrite(pinLED, HIGH);
  } else {
    digitalWrite(pinLED, LOW);
  }
  delay(100);
}
