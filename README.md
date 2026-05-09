# LegoEv3 — *Autonomous Navigation Robot

A Python-based autonomous robot built on the LEGO Mindstorms EV3 platform. The robot uses touch sensors for collision detection and an infrared sensor mounted on a rotating lever motor to perform LIDAR-inspired environment scanning, displaying a real-time contour map on the EV3 screen.

---

## Hardware

| Component | Port | Role |
|---|---|---|
| Left Drive Motor | A | Locomotion |
| Right Drive Motor | D | Locomotion |
| Lever Motor | B | Rotates the infrared sensor ±180° |
| Left Touch Sensor | S1 | Detects left-side collisions |
| Right Touch Sensor | S4 | Detects right-side collisions |
| Infrared Sensor | S3 | Measures distance for environment scanning |

**Robot configuration:**
- Wheel diameter: 55.5 mm
- Axle track: 106 mm
- The infrared sensor is mounted on the lever motor, positioned above the EV3 screen, and sweeps ±180° like a LIDAR unit.

---

## Project Structure

```
LegoEv3/
├── src/
│   ├── robot/
│   │   ├── __init__.py
│   │   └── core.py       # All robot logic and classes
│   └── main.py           # Entry point — instantiates Robot and calls methods
└── README.md
```

---

## Features

### Collision Detection — `drive_until_collision()`
The robot drives forward and reacts to touch sensor input in real time:
- **No contact** → drives straight
- **Left sensor only** → turns right
- **Right sensor only** → turns left
- **Both sensors** → stops, backs up, and exits

### LIDAR-Inspired Scanning — `Infrared_scan()`
The lever motor sweeps the infrared sensor from 0° to -180°, then from 0° to +180°, continuously. For each angle:
- The sensor reads distance `r`
- Polar coordinates `(r, θ)` are converted to screen coordinates `(x, y)`
- A line is drawn from the robot's position to the detected point
- A red dot marks the surface of detected objects
- A green dot marks the robot's position at the center

This produces a real-time contour map of the surrounding environment on the EV3's 178×128 px screen.

### Startup Gate — `pause_until_Ts_pressed()`
The robot waits for either touch sensor to be pressed before starting any routine, with a 2-second delay to allow the operator to step back.

---

## Dependencies

- [Pybricks](https://pybricks.com/) — EV3 MicroPython firmware
- Python `math` module (included in Pybricks)

> This project runs on **Pybricks MicroPython**, not standard CPython. 



 






