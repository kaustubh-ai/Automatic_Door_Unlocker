

# Automatic Door Unlocker

### Table of Contents

- [Project Motivation](#motivation)
- [Project Components](#components)
  - [Encoding Images](#encode_image)
  - [Comparing Faces](#compare_face)
  - [Arduino](#arduino)
- [Usage](#usage)
- [Contribute](#contribute)

***

<a id='motivation'></a>

## 1. Project Motivation

Wish there was a smart enough lock that automatically opens when someone you recognise is at the door? Look no further 'cause here it is!

<a id='components'></a>

## 2. Project Components

There are three components in this project:

<a id='encode_image'></a>

### 2.1. Encoding Images

File `encode_image.py` contains the code to encode images. It uses the `face_recognition` library that is a Python wrapper for the `dlib` library (written in C++) . This dlib library consists of a pre-trained deep neural network trained on roughly 3 million images to convert image into 128 dimensional vectors that are actually face embeddings storing information about various facial features like eyes, nose, etc.  The directory structure for the images you wish to train upon is './data/train'. See repo for more. This fianlly creates a `encodings.pickle` file that stores the encodings.

<a id='compare_face'></a>

### 2.2. Comparing Faces

File `face_recognise.py` contains the code to compare faces. It calculates the eucledian distance between the image vectors using `np.linalg.norm` from numpy. 
- If the distance is below some tolerance (the smaller the tolerance, the more strict the facial recognition system will be) then we return `True`, indicating the faces match.
-   Otherwise, if the distance is above the tolerance threshold, we return `False` as the faces do not match.
<br>
This file also contains code that sends the proper signal to the arduino to switch on / switch off the motor based on the face recognition model's output.

<a id='arduino'></a>

### 2.3. Arduino

File `motor.ino` contains the arduino code (written in C++) to automatically control the opening and closing of the door. Utilises the arduino pins to send signals to the motor. The USB port is used to send the signal from the laptop to the arduino.

***

<a name="usage"/>

## Usage

<a id='local'></a>

Run the file `face_recognise`. Enter '1' for  laptop's built-in webcam or '2' for a wireless webcam. Be sure to enter the correct IP of your webcam in the wireless case. 
It will output the name of the person on the console if it is a correct match.
***

<a name="contribute"/>

## Contribute
1.  Fork the repository from Github
2.  Clone your fork

`git clone https://github.com/kaustubh-ai/Automatic_Door_Unlocker.git`

3.  Add the main repository as a remote

```git remote add upstream https://github.com/kaustubh-ai/Automatic_Door_Unlocker.git```

4.  Create a pull request!
