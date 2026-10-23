int led=13;
int n=0;
int i=0;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.println("Escriu un numero:");
}

void loop() {
  if (Serial.available() > 0) {
    n = Serial.parseInt();
    if (n > 0) {
      Serial.print("El led s'encendra ");
      Serial.print(n);
      Serial.println(" vegades");
      for (i=0; i<n; i++) {
        digitalWrite(led, HIGH);
        delay(500);
        digitalWrite(led, LOW);
        delay(500);
      }
      Serial.println("Escriu un altre numero:");
    }
  }
}
