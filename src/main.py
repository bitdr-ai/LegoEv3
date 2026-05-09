#!/usr/bin/env pybricks-micropython
from robot.core import Robot
from pybricks.parameters import Port, Color
from pybricks.tools import wait
import math

robot = Robot()

robot.ev3.speaker.beep()
robot.Infrared_scan()

