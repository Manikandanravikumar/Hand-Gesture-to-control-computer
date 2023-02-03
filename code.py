Arduino Code:

int trigPin1 = 6; // Trigger
int echoPin1 =7; // Echo
int trigPin2 =8; // Trigger
int echoPin2 =9; // Echo
long duration1, cm1,duration2,cm2;
void setup() {
Serial.begin (9600);
pinMode(trigPin1, OUTPUT);
pinMode(echoPin1, INPUT);
pinMode(trigPin2, OUTPUT);
pinMode(echoPin2, INPUT);

}
void loop() {
// The sensor is triggered by a HIGH pulse of 10 or more microseconds.
// Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
digitalWrite(trigPin1, LOW);
delayMicroseconds(5);
digitalWrite(trigPin1, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin1, LOW);
// Read the signal from the sensor: a HIGH pulse whose
// duration is the time (in microseconds) from the sending
// of the ping to the reception of its echo off of an object.
pinMode(echoPin1, INPUT);
duration1 = pulseIn(echoPin1, HIGH);
// Convert the time into a distance
cm1 = (duration1/2) / 29.1; // Divide by 29.1 or multiply by 0.0343
digitalWrite(trigPin2, LOW);
delayMicroseconds(5);
digitalWrite(trigPin2, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin2, LOW);
// Read the signal from the sensor: a HIGH pulse whose
// duration is the time (in microseconds) from the sending
// of the ping to the reception of its echo off of an object.

pinMode(echoPin2, INPUT);
duration2 = pulseIn(echoPin2, HIGH);

// Convert the time into a distance
cm2= (duration2/2) / 29.1; // Divide by 29.1 or multiply by 0.0343
if(cm1<9)
{
  Serial.println("screenShot");
  delay(1000);
}
else if(cm2<9)
{
  Serial.println("DoubleClick");
  delay(1000);
}
else if(cm1> 10 && cm1<26)
{//back
  Serial.println("back");
  delay(1000);
}
else if(cm2> 10 && cm2<23)
{// next
  Serial.println("next");
  delay(1000);
}
else if((cm1>=7 && cm1<35) && (cm2>=7 && cm2<35)){
  Serial.println("DoubleClick");
  delay(1000);
}
else if(cm1>27 && cm1<35)
{//UPKey
  Serial.println("DOWNKey");
  delay(1000);
}
else if(cm2>27 && cm2<35)
{//DOWNKey
  Serial.println("UPKey");
  delay(1000);  
}
}





Python code:
import serial  # Serial imported for Serial communication
import time  # Required to use delay functions
import pyautogui

ArduinoSerial = serial.Serial('COM3', 9600)  # Create Serial port object called arduinoSerialData
time.sleep(2)  # wait for 2 seconds for the communication to get established
i=3;
while 1:
    incoming = str(ArduinoSerial.readline())  # read the serial data and print it as line
    print(incoming)



    if 'back' in incoming:  # cm1<15
        pyautogui.press('left')

    elif 'UPKey' in incoming:  # cm1>=20 &&cm1<40
        pyautogui.hotkey('ctrl', 'up')

    elif 'DOWNKey' in incoming:  # cm2>=20 &&cm2<40
        pyautogui.hotkey('ctrl', 'down')

    elif 'next' in incoming:  # cm2<15
        pyautogui.press('right')

    elif 'screenShot' in incoming:  # cm1<10 && cm2<10

        pyautogui.press('ctrl')
        pyautogui.press('printscreen')
    elif 'DoubleClick' in incoming:  # cm1>=20 &&cm1<40 && cm2>=20 &&cm2<40
        pyautogui.press('enter')
        pyautogui.press('space')

    elif 'TabChange' in incoming:  # cm1<20 && cm2>40
        print('TabChange')
        #
        # pyautogui.keyDown('alt')
        # time.sleep(2)
        # pyautogui.press('tab')
        # time.sleep(2)
        # pyautogui.keyUp('alt')
incoming = ""
