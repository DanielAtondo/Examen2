char option = ' ';
int LED = 7;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if(Serial.available() != 0){
    option = Serial.read();
    if(option == '1'){
      digitalWrite(LED_BUILTIN, HIGH);
      digitalWrite(LED, HIGH);
    }

    else if(option == '0'){
      digitalWrite(LED_BUILTIN, LOW);
      digitalWrite(LED, LOW);
    }
  }
  
  delay(100);
}
