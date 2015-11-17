int incomingByte = 0; // almacenar el dato serie

//  MOTOR 1
int E1 = 6;
int M1 = 7;
// MOTOR 2
int E2 = 5;                        
int M2 = 4;    

void setup() {
Serial.begin(9600); // abre el puerto serie,y le asigna la velocidad de 9600 bps

pinMode(M1, OUTPUT);  
pinMode(M2, OUTPUT);
    
}
void loop() {
  
// envía datos sólo si los recibe:
  if (Serial.available() > 0) {
      // lee el byte de entrada:
      incomingByte = Serial.read();
      //muestro el dato en el monitor serial
      Serial.println(incomingByte, DEC);
      
  }

  switch(incomingByte) {
    
    case 50: // Avanza 
       digitalWrite(M1,HIGH);
        digitalWrite(M2,HIGH);
         delay(100);
        digitalWrite(M1,LOW);
        digitalWrite(M2,LOW);
        break;
 case 51:  // Retrocede 
        digitalWrite(E1,HIGH);
        digitalWrite(E2,HIGH);
         delay(100);
        digitalWrite(E1,LOW);
        digitalWrite(E2,LOW);
        break;
        
 case 52:  // GIRA izquierda 
        digitalWrite(E2,HIGH);
        digitalWrite(M1,HIGH);
         delay(100);
         digitalWrite(E2,LOW);       
        digitalWrite(M1,LOW);
        break;
        
  case 53:  // GIRA Derecha
        digitalWrite(E1,HIGH);
        digitalWrite(M2,HIGH);
         delay(100);
         digitalWrite(E1,LOW);       
        digitalWrite(M2,LOW);
        break;
      
     default:
        // si no llega ninguna orden particular, apago los motores 
        digitalWrite(M1,LOW);
        digitalWrite(M2,LOW);
        break;
       
}
}
