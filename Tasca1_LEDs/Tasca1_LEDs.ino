/*
  Robòtica - Tasca 1.1 LEDs
  Autors: Pau Martínez Cuadra i Enric Vinyes Huguet

  Utilitzem 7 leds connectats als ports 4, 5, 6, 7, 8, 9 i 10.

    LED:    led-1 led-2 led-3 led-4 led-5 led-6 led-7
    Port:     4     5     6     7     8     9     10
    Tipus:   senar parell senar parell senar parell senar

  Funcionament:
  - D'esquerra a dreta s'encenen només els leds senars: led-1, led-3, led-5, led-7
    (ports 4, 6, 8, 10).
  - De dreta a esquerra s'encenen només els leds parells: led-6, led-4, led-2
    (ports 9, 7, 5).
  Cada led està encès durant "temps" mil·lisegons i després s'apaga.
  Fem servir dos llaços "for" que avancen de 2 en 2 per saltar-nos un led cada vegada.
*/

int temps = 200;  // temps (en mil·lisegons) que cada led està encès i apagat

void setup() {
  // inicialitzem tots els ports del 4 al 10 com a SORTIDA
  for (int x = 4; x <= 10; x++) {
    pinMode(x, OUTPUT);
  }
}

void loop() {
  // esquerra -> dreta: leds senars (ports 4, 6, 8, 10)
  for (int x = 4; x <= 10; x = x + 2) {
    digitalWrite(x, HIGH);
    delay(temps);
    digitalWrite(x, LOW);
    delay(temps);
  }

  // dreta -> esquerra: leds parells (ports 9, 7, 5)
  for (int x = 9; x >= 5; x = x - 2) {
    digitalWrite(x, HIGH);
    delay(temps);
    digitalWrite(x, LOW);
    delay(temps);
  }
}
