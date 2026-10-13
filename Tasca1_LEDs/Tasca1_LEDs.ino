int temps=200;

void setup() {
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {
  for (int x=4; x<=10; x=x+2) {
    digitalWrite(x, HIGH);
    delay(temps);
    digitalWrite(x, LOW);
    delay(temps);
  }
  for (int x=9; x>=5; x=x-2) {
    digitalWrite(x, HIGH);
    delay(temps);
    digitalWrite(x, LOW);
    delay(temps);
  }
}
