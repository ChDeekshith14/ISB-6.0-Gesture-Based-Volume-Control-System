## **Gesture-Based-Volume-Control-System**

---

## ✋ Hand Gesture Based Volume Control System

An interactive computer vision application that allows users to control system volume using hand gestures captured through a webcam. The system uses MediaPipe for hand landmark detection and OpenCV for real-time video processing, enabling touchless interaction with a computer.

By calculating the distance between specific finger landmarks, the system interprets gestures and dynamically adjusts the system volume using Python automation libraries. A Flask-based interface displays the live camera feed and gesture status, improving usability.

This project demonstrates a practical implementation of Human-Computer Interaction (HCI) using computer vision techniques.

---

## 🎯 Project Objective

The objective of this project is to design and develop a touchless volume control system that enables users to adjust system audio using hand gestures.

The system reduces physical interaction with traditional hardware devices such as keyboards or mice and provides a more intuitive, hygienic, and user-friendly interface. It is especially useful in environments where physical input devices are inconvenient or inaccessible.

---

## ⚠️ Problem Statement

Traditional volume control methods require physical interaction with input devices, which may not always be convenient or hygienic.

In modern smart environments, users increasingly prefer contactless interaction systems. Existing systems do not provide natural gesture-based control for basic functions like adjusting system volume.

The challenge is to create a real-time gesture recognition system that allows users to control system audio using hand movements captured through a webcam.

---

## 💡 Proposed Solution

The proposed system uses computer vision and hand gesture recognition to enable touchless volume control.

The webcam captures live video input, which is processed using OpenCV. Hand landmarks are detected using MediaPipe, and the distance between specific finger points is calculated to determine the user's gesture.

The gesture is then mapped to the system’s volume level, and the volume is automatically adjusted using Python automation libraries. A Flask web interface provides a real-time view of the camera feed and gesture detection status.

----

## 🛠️ Technologies Used

- Programming Language - Python
- Libraries & Tools
- OpenCV – Real-time video capture and image processing
- MediaPipe – Hand tracking and landmark detection
- PyAutoGUI – System automation for controlling volume
- NumPy – Numerical operations and calculations
- Math Functions – Distance calculations between finger landmarks

---

## ⚙️ System Architecture / Workflow

- The system operates through the following workflow:
- Webcam captures live video frames.
- OpenCV processes the incoming frames.
- MediaPipe detects and tracks hand landmarks.
- Specific finger landmark positions are identified.
- Distance between fingers is calculated using Euclidean distance.
- Gesture is interpreted based on the calculated distance.
- Python automation library adjusts the system volume.
- Flask interface displays real-time gesture feedback and camera feed.

---

## ✨ Key Features

- Real-time hand detection using MediaPipe
- Gesture-based system volume control
- Live webcam video processing
- Real-time interaction with minimal latency
- Flask-based interface for visual feedback
- Practical implementation of Human-Computer Interaction concepts

---

## 🚧 Challenges Faced

- Achieving accurate hand detection under varying lighting conditions
- Preventing unintended volume changes caused by random hand movements
- Maintaining smooth real-time performance without system lag
- Handling detection when multiple hands appear in the frame

---

## 📚 Skills & Learnings

- Real-time computer vision development using OpenCV
- Hand landmark detection using MediaPipe
- Gesture recognition implementation
- Python automation and system control
- Integration of Flask for simple web interfaces
- Debugging and optimizing real-time applications

---

## 📸 Screenshots
🔧 Code Execution

(Add screenshot of the program running in terminal or IDE)

images/code_execution.png
🎥 Live Gesture Detection

(Add screenshot showing webcam feed with hand landmarks)

images/gesture_detection.png
🔊 System Output

(Add screenshot showing volume control working)

images/output.png

---

## 📌 Future Scope

 - Voice and gesture hybrid control system
 - Mobile device integration
 - AI-based gesture classification using deep learning models
 - Support for additional gesture commands such as mute or media control
 - Integration with smart home or IoT systems

---

## 🙏 Acknowledgements

We sincerely thank Infosys Springboard Virtual Internship Program, mentors, and academic coordinators for their guidance and support throughout the internship.
