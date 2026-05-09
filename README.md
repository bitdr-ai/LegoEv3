# LEGO EV3 Project
Version: v1.3

Robotics project developed for LEGO EV3 using Python with Pybricks on ev3dev OS.
This project evolves from basic motion control to environment perception and mapping using onboard sensors and motor-based scanning.


## Hardware
- LEGO EV3 Brick  
- Two drive motors (Ports A and D)  
- Medium motor for sensor rotation (Port B)  
- Touch sensors (Ports S1 and S4)  
- Infrared sensor (Port S3)  
- Wheel diameter: 55.5 mm  
- Axle track: 106 mm  

## Software
- ev3dev OS
- Pybricks MicroPython
- Python 3

## System Overview

The robot is built on a differential-drive model and integrates multiple sensing and mapping strategies:

- Reactive navigation using touch sensors  
- Distance estimation using infrared sensing  
- Angular scanning via a rotating sensor platform  
- Basic 2D mapping using odometry and collision detection  

---

## Features

### Motion & Navigation
- Forward motion using `DriveBase`
- Differential turning
- Collision detection and avoidance
- Reactive behavior based on touch input

### Infrared Polar Mapping
- Rotating sensor using a dedicated motor
- Angular sweep with real motor angle feedback
- Conversion from polar to Cartesian coordinates:
  - distance + angle → (x, y)
- Real-time visualization on EV3 display (radar-like)

### Grid / Path Mapping (Experimental)
- Movement until collision
- Distance tracking using wheel odometry
- Step-by-step path reconstruction
- Line-based map drawing on screen

---

## Current Limitations
- Infrared sensor noise and low precision  
- No filtering of distance measurements  
- Mapping is local (no persistent storage)  
- No global coordinate system alignment  

---

## Current Focus
- Improving infrared-based mapping accuracy  
- Stabilizing angular scanning  
- Refining coordinate calculations  
- Reducing measurement noise  

---

## Future Work
- Point cloud generation  
- Persistent environment mapping  
- Sensor fusion (IR + odometry)  
- Autonomous navigation  
- Path planning algorithms  

---
