#!/usr/bin/env pybricks-micropython
from robot.core import Robot
from pybricks.parameters import Port, Color
from pybricks.tools import wait
import math

robot = Robot()

robot.ev3.screen.print("Press touch sensor to start")
robot.pause_until_Ts_pressed()
robot.ev3.screen.clear()
robot.ev3.speaker.beep()


robot.ev3.screen.draw_circle(87, 123, 4, True, Color.GREEN) 
robot.lever_motor.run_target(105, 90, wait=True)
robot.lever_motor.reset_angle(0)

while True:
    robot.lever_motor.run_angle(105, -10)
    theta = robot.lever_motor.angle()
    r = robot.Infrared_S.distance() *0.8

    x2 = r*math.cos(math.radians(theta))
    y2 = r*math.sin(math.radians(theta))
    
    robot.ev3.screen.draw_line(87, 123, x2, y2, width=1, color=Color.BLACK)
    wait(50)

    print("theta:", theta, "x2:", x2, "y2:", y2)

    if theta <= -180:
        break
    wait(20)
