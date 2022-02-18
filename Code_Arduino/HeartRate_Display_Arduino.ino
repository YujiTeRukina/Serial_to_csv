int Signal;                             

void setup() {
  // initialize the serial communication:
  Serial.begin(9600);
  pinMode(10, INPUT); // Setup for leads off detection LO +
  pinMode(11, INPUT); // Setup for leads off detection LO -

}

void loop() {
  
  Signal = analogRead(A0); 

  if ((digitalRead(10) == 1) || (digitalRead(11) == 1)) {
    Serial.println(0);
  }
  else {
    // send the value of analog input 0:
    Serial.println(Signal);
  }

  //Wait for a bit to keep serial data from saturating
  delay(1);
}
