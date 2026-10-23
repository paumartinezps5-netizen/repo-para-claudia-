// C++ code
//
void setup()
{
pinMode(13,OUTPUT);
pinMode(12,OUTPUT);
pinMode(11,OUTPUT);

pinMode(9,OUTPUT);
pinMode(8,OUTPUT);
}
void loop()
{
digitalWrite(11,HIGH);
digitalWrite(9,HIGH);
delay(5000);
digitalWrite(11,LOW);
digitalWrite(12,HIGH);
delay(1500);
digitalWrite(12,LOW);
digitalWrite(13,HIGH);
delay(1000);
digitalWrite(9,LOW);
digitalWrite(8,HIGH);
delay(3000);

digitalWrite(8,LOW);
delay(300);
digitalWrite(8,HIGH);
delay(300);
digitalWrite(8,LOW);
delay(300);
digitalWrite(8,HIGH);
delay(300);
digitalWrite(8,LOW);
digitalWrite(9,HIGH);
delay(1000);
digitalWrite(13,LOW);
}
