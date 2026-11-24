// C++ code
//
int i=0;
void setup()
{
 pinMode(13,OUTPUT);
 pinMode(12,OUTPUT);
 pinMode(11,OUTPUT);
 pinMode(9,OUTPUT);
 pinMode(8,OUTPUT);
 pinMode(7,INPUT);
 pinMode(3,OUTPUT);
}
void loop()
{
 digitalWrite(11,HIGH);
 digitalWrite(9,HIGH);
 if (digitalRead(7)==HIGH) {
 delay(2000);
 digitalWrite(11,LOW);
 digitalWrite(12,HIGH);
 delay(1500);
 digitalWrite(12,LOW);
 digitalWrite(13,HIGH);
 delay(1000);
 digitalWrite(9,LOW);
 digitalWrite(8,HIGH);
 for (i=0; i<3; i++) {
 digitalWrite(3,HIGH);
 delay(200);
 digitalWrite(3,LOW);
 delay(600);
 }
 for (i=0; i<4; i++) {
 digitalWrite(8,HIGH);
 digitalWrite(3,HIGH);
 delay(300);
 digitalWrite(8,LOW);
 digitalWrite(3,LOW);
 delay(300);
 }
 for (i=0; i<6; i++) {
 digitalWrite(8,HIGH);
 digitalWrite(3,HIGH);
 delay(150);
 digitalWrite(8,LOW);
 digitalWrite(3,LOW);
 delay(150);
 }
 for (i=0; i<8; i++) {
 digitalWrite(8,HIGH);
 digitalWrite(3,HIGH);
 delay(75);
 digitalWrite(8,LOW);
 digitalWrite(3,LOW);
 delay(75);
 }
 digitalWrite(8,HIGH);
 digitalWrite(3,HIGH);
 delay(1000);
 digitalWrite(3,LOW);
 digitalWrite(8,LOW);
 digitalWrite(9,HIGH);
 delay(1000);
 digitalWrite(13,LOW);
 }
}
