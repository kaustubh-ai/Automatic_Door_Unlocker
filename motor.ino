const int led=3;
int value=0;

void setup() 
   { 
      Serial.begin(9600); 
      pinMode(led, OUTPUT);
      digitalWrite (led, LOW);
      Serial.println("Connection established...");
   }
 
void loop() 
   {
     while (Serial.available())
        {
           value = Serial.read();
        }
     
     if (value == '1')
//        digitalWrite (led, HIGH);
          analogWrite(led, 120);
     
     else if (value == '0')
        digitalWrite (led, LOW);
   }
