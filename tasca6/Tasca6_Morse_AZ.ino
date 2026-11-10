  int led13 = 13;
  int val = 0;
  int EncesaLlarga = 200;
  int EncesaCurta = 100;
  int PausaLletra = 1000;

  void punt(){
    digitalWrite(led13,HIGH);
    delay(EncesaCurta);
    digitalWrite(led13,LOW);
    delay(EncesaCurta);
    Serial.println("punt");
  }

  void ratlla(){
    digitalWrite(led13,HIGH);
    delay(EncesaLlarga);
    digitalWrite(led13,LOW);
    delay(EncesaLlarga);
    Serial.println("ratlla");
  }

void setup() {
  pinMode (led13,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0){
    val = Serial.read(); 
    switch(val){
        case 'A':
        case 'a':
          punt();
          ratlla();
          delay(PausaLletra);
          break;

        case 'B':
        case 'b':
          ratlla();
          punt();
          punt();
          punt();
          delay(PausaLletra);
          break;

        case 'C':
        case 'c':
          ratlla();
          punt();
          ratlla();
          punt();
          delay(PausaLletra);
          break;

        case 'D':
        case 'd':
          ratlla();
          punt();
          punt();
          delay(PausaLletra);
          break;

        case 'E':
        case 'e':
          punt();
          delay(PausaLletra);
          break;

        case 'F':
        case 'f':
          punt();
          punt();
          ratlla();
          punt();
          delay(PausaLletra);
          break;

        case 'G':
        case 'g':
          ratlla();
          ratlla();
          punt();
          delay(PausaLletra);
          break;

        case 'H':
        case 'h':
          punt();
          punt();
          punt();
          punt();
          delay(PausaLletra);
          break;

        case 'I':
        case 'i':
          punt();
          punt();
          delay(PausaLletra);
          break;

        case 'J':
        case 'j':
          punt();
          ratlla();
          ratlla();
          ratlla();
          delay(PausaLletra);
          break;

        case 'K':
        case 'k':
          ratlla();
          punt();
          ratlla();
          delay(PausaLletra);
          break;

        case 'L':
        case 'l':
          punt();
          ratlla();
          punt();
          punt();
          delay(PausaLletra);
          break;

        case 'M':
        case 'm':
          ratlla();
          ratlla();
          delay(PausaLletra);
          break;

        case 'N':
        case 'n':
          ratlla();
          punt();
          delay(PausaLletra);
          break;

        case 'O':
        case 'o':
          ratlla();
          ratlla();
          ratlla();
          delay(PausaLletra);
          break;

        case 'P':
        case 'p':
          punt();
          ratlla();
          ratlla();
          punt();
          delay(PausaLletra);
          break;

        case 'Q':
        case 'q':
          ratlla();
          ratlla();
          punt();
          ratlla();
          delay(PausaLletra);
          break;

        case 'R':
        case 'r':
          punt();
          ratlla();
          punt();
          delay(PausaLletra);
          break;

        case 'S':
        case 's':
          punt();
          punt();
          punt();
          delay(PausaLletra);
          break;

        case 'T':
        case 't':
          ratlla();
          delay(PausaLletra);
          break;

        case 'U':
        case 'u':
          punt();
          punt();
          ratlla();
          delay(PausaLletra);
          break;

        case 'V':
        case 'v':
          punt();
          punt();
          punt();
          ratlla();
          delay(PausaLletra);
          break;

        case 'W':
        case 'w':
          punt();
          ratlla();
          ratlla();
          delay(PausaLletra);
          break;

        case 'X':
        case 'x':
          ratlla();
          punt();
          punt();
          ratlla();
          delay(PausaLletra);
          break;

        case 'Y':
        case 'y':
          ratlla();
          punt();
          ratlla();
          ratlla();
          delay(PausaLletra);
          break;

        case 'Z':
        case 'z':
          ratlla();
          ratlla();
          punt();
          punt();
          delay(PausaLletra);
          break;
     }
  }
}
