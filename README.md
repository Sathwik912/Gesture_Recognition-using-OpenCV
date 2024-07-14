# Gesture_Recognition-using-OpenCV
Gesture-Controlled Servo Motor project combines computer vision and hardware interfacing to create an interactive system. Using hand gestures  captured by a webcam, users can control the position of a servo motor in real- time.


# Software Libraries
* Python 3.7-3.9
* OpenCV
* mediapipe
* pyFirmata

Note: Python version 3.7-3.9 is chosen for this project due to its compatibility with the pyFirmata library, which is crucial for communication between the computer and Arduino board.

# Arduino IDE
1. open the Arduino IDE on your computer.
2. Navigate to the "Sketch" menu and select "Include Library" -> "Manage Libraries...".
3. In the Library Manager window, type "Firmata" in the search bar, locate the "Firmata by Firmata Developers" library, and click the "Install" button.
4. Once the installation is complete, go to "File" -> "Examples" -> "Firmata" -> "StandardFirmata" and upload the StandardFirmata sketch to your Arduino Uno board. This sketch enables the Arduino to communicate with the Python script using the Firmata protocol.

# Circuit Diagram 
![circuit ](https://github.com/user-attachments/assets/36e2ab2c-4ba6-4b3e-9211-1f24724d1585)

# Testing and Results 
![Gesture model demo pic](https://github.com/user-attachments/assets/03c6c171-a02e-4b72-9185-ed9e3c0e2d3d)




