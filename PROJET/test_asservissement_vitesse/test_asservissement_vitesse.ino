#include <SimpleTimer.h>
#define LEFT 0
#define RIGHT 1


SimpleTimer timer;

int speedPin_M1 = 5;     //M1 Speed Control
int speedPin_M2 = 6;     //M2 Speed Control
int directionPin_M1 = 4;     //M1 Direction Control
int directionPin_M2 = 7;     //M1 Direction Control

long coder[2] = {
  0,0};

float consigne_vitesse = 1; //1 tour par seconde
const int nombre_tick_par_tour_codeuse = 20;
const int freq_ech = 1000;
int cmd_initiale = 100;

//coeffs du correcteur
float kp_L = 15 ;
float ki_L = 0;
float kd_L = 0;

// erreurs
float erreur_L;
float erreur_L_precedente = consigne_vitesse;
float somme_erreur_L = 0;
float delta_erreur_L;

//commandes
int cmd_L = 0;

void setup() {
  Serial.begin(9600);                            //init the Serial port to print the data
  attachInterrupt(LEFT, LwheelSpeed, CHANGE);    //init the interrupt mode for the digital pin 2
  attachInterrupt(RIGHT, RwheelSpeed, CHANGE);   //init the interrupt mode for the digital pin 3
  timer.setInterval(freq_ech,asservissement_vitesse);
}

void loop() {

   carAdvance(cmd_initiale,cmd_initiale);
   delay(2400);
   carStop();
   delay(500);
    
  // Partie qui gère l'acquisition des données des encodeurs
  static unsigned long timer = 0;                //print manager timer
  static unsigned long duree = millis() - timer;
  
  if(duree > 100){                   
    //Serial.print("Nb changements sur la durée d'acquisition: ");
    //Serial.print(coder[LEFT]);
    //Serial.print("[Left Wheel] ");
    //Serial.print(coder[RIGHT]);
    //Serial.println("[Right Wheel]");

    float nombre_tour_gauche = coder[LEFT]/nombre_tick_par_tour_codeuse;
    float nombre_tour_droite = coder[RIGHT]/nombre_tick_par_tour_codeuse;

    float vitesse_gauche = nombre_tour_gauche / (duree*10E-3);
    float vitesse_droite = nombre_tour_droite / (duree*10E-3);

    Serial.print(nombre_tour_gauche);
    Serial.println("[nb tour gauche]");
    Serial.println(vitesse_gauche); //calcule pas la vitesse ...

    coder[LEFT] = 0;                 //clear the data buffer
    coder[RIGHT] = 0;
    timer = millis();
  }
}

void LwheelSpeed(){
  coder[LEFT] ++;  //count the left wheel encoder interrupts
}


void RwheelSpeed(){
  coder[RIGHT] ++; //count the right wheel encoder interrupts
}

void asservissement_vitesse(float vitesse_gauche){
  erreur_L = consigne_vitesse - vitesse_gauche;
  delta_erreur_L = erreur_L - erreur_L_precedente;
  somme_erreur_L += erreur_L;
  erreur_L_precedente = erreur_L;

  //Calcul de la commande
  cmd_L = kp_L * erreur_L + kd_L * delta_erreur_L + ki_L * somme_erreur_L;

  // Controle du moteur
  if (cmd_L < 0) cmd_L=cmd_L/10; // on ralentit le moteur car il va trop vite
  else if (cmd_L > 0) cmd_L = cmd_initiale + cmd_L; // il faut accélérer le moteur car il va trop lentement
  analogWrite(speedPin_M1,cmd_L);
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
