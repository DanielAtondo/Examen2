// C++ code
//
void setup()
{
  Serial.begin(9600);
  pinMode(7, INPUT);
}

void loop()
{
 if(digitalRead(7) == HIGH){Serial.println("1");}
 else {Serial.println("0");}
}
