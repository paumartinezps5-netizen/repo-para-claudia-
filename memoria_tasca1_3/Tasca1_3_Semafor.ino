// Semàfor bàsic: 3 leds pels cotxes i 2 pels vianants

int vermellCotxes = 13;
int grocCotxes = 12;
int verdCotxes = 11;
int vermellVianants = 9;
int verdVianants = 8;

void setup()
{
  // Tots els leds són sortides
  pinMode(vermellCotxes, OUTPUT);
  pinMode(grocCotxes, OUTPUT);
  pinMode(verdCotxes, OUTPUT);
  pinMode(vermellVianants, OUTPUT);
  pinMode(verdVianants, OUTPUT);
}

void loop()
{
  // 1. Verd pels cotxes i vermell pels vianants durant 5 s
  digitalWrite(vermellCotxes, LOW);
  digitalWrite(verdCotxes, HIGH);
  digitalWrite(vermellVianants, HIGH);
  delay(5000);

  // 2. Es passa a groc directament. Els vianants segueixen en vermell
  digitalWrite(verdCotxes, LOW);
  digitalWrite(grocCotxes, HIGH);
  delay(2000);

  // 3. Vermell pels cotxes. Esperem 1 s amb els dos vermells per seguretat
  digitalWrite(grocCotxes, LOW);
  digitalWrite(vermellCotxes, HIGH);
  delay(1000);

  // 4. Verd pels vianants durant 3 s
  digitalWrite(vermellVianants, LOW);
  digitalWrite(verdVianants, HIGH);
  delay(3000);

  // 5. El verd dels vianants fa pampallugues 3 cops per avisar que s'acaba
  digitalWrite(verdVianants, LOW);
  delay(300);
  digitalWrite(verdVianants, HIGH);
  delay(300);
  digitalWrite(verdVianants, LOW);
  delay(300);
  digitalWrite(verdVianants, HIGH);
  delay(300);
  digitalWrite(verdVianants, LOW);
  delay(300);
  digitalWrite(verdVianants, HIGH);
  delay(300);
  digitalWrite(verdVianants, LOW);

  // 6. Vermell pels vianants i 1 s amb els dos vermells abans de tornar a començar
  digitalWrite(vermellVianants, HIGH);
  delay(1000);
}
