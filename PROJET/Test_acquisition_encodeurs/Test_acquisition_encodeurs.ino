// # Connection:
// #        left wheel encoder  -> Digital pin 2
// #        right wheel encoder -> Digital pin 3
// #
// PARAMETRE POUR FAIRE UN NOMBRE ENTIER DE TOUR DE ROUE
//1 TOUR:
//alim 100 et delay 1200


#define LEFT 0
#define RIGHT 1

int speedPin_M1 = 5;     //M1 Speed Control
int speedPin_M2 = 6;     //M2 Speed Control
int directionPin_M1 = 4;     //M1 Direction Control
int directionPin_M2 = 7;     //M1 Direction Control

long coder[2] = {
  0,0};
//int lastSpeed[2] = {
  //0,0};  


void setup(){

  Serial.begin(9600);                            //init the Serial port to print the data
  attachInterrupt(LEFT, LwheelSpeed, CHANGE);    //init the interrupt mode for the digital pin 2
  attachInterrupt(RIGHT, RwheelSpeed, CHANGE);   //init the interrupt mode for the digital pin 3

}

void loop(){

    carAdvance(100,100);
    delay(1200);
    carStop();
    delay(500);

  static unsigned long timer = 0;                //print manager timer
  static unsigned long duree = millis() - timer;
  
  if(duree > 100){                   
    Serial.print("Nb changements sur 100 ms: ");
    Serial.print(coder[LEFT]);
    Serial.print("[Left Wheel] ");
    Serial.print(coder[RIGHT]);
    Serial.println("[Right Wheel]");

    float nombre_tour_gauche = coder[LEFT]/20;
    float nombre_tour_droite = coder[RIGHT]/20;

    float vitesse_gauche = nombre_tour_gauche / (duree*10E-3);
    float vitesse_droite = nombre_tour_droite / (duree*10E-3);

    Serial.print(nombre_tour_gauche,4);
    Serial.println("[nb tour gauche]");
    Serial.println(vitesse_gauche,4); //calcule pas la vitesse ...
    //Serial.print(duree);
    //Serial.println("[Vitesse droite]");
    

    //lastSpeed[LEFT] = coder[LEFT];   //record the latest speed value
    //lastSpeed[RIGHT] = coder[RIGHT];
    coder[LEFT] = 0;                 //clear the data buffer
    coder[RIGHT] = 0;
    timer = millis();
  }
}


void LwheelSpeed()
{
  coder[LEFT] ++;  //count the left wheel encoder interrupts
}


void RwheelSpeed()
{
  coder[RIGHT] ++; //count the right wheel encoder interrupts
}

void carStop(){                 //  Motor Stop
  digitalWrite(speedPin_M2,0);
  digitalWrite(directionPin_M1,LOW);
  digitalWrite(speedPin_M1,0);
  digitalWrite(directionPin_M2,LOW);
}

void carAdvance(int leftSpeed,int rightSpeed){       //Move forward
  analogWrite (speedPin_M2,leftSpeed);
  digitalWrite(directionPin_M1,HIGH);
  analogWrite (speedPin_M1,rightSpeed);
  digitalWrite(directionPin_M2,LOW);
}
