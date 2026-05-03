#core.py
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait
import math

class Robot:
    def __init__(self):
        #EV3
        self.ev3 = EV3Brick() 
        
        #Motors
        self.left_motor = Motor(Port.A)
        self.right_motor = Motor(Port.D)
        self.lever_motor = Motor(Port.B)

        #Sensors 
        self.left_Tsensor = TouchSensor(Port.S1)
        self.right_Tsensor = TouchSensor(Port.S4)
        self.Infrared_S = InfraredSensor(Port.S3)

        #DriveBase
        self.drivebase = DriveBase(self.left_motor, self.right_motor, wheel_diameter=55.5, axle_track=106)

    #Methods
    def pause_until_Ts_pressed(self):
        while True:
            if self.left_Tsensor.pressed() or self.right_Tsensor.pressed():
                break
        wait(2000)


    def drive_until_collision(self):
        while True:
            left = self.left_Tsensor.pressed()
            right = self.right_Tsensor.pressed()

            if left==0 and right==0:
                self.drivebase.drive(100,0)

            elif left==1 and right==0:
                self.drivebase.drive(0, -50)

            elif left==0 and right==1:
                self.drivebase.drive(0, 50)
            
            elif left and right:
                self.drivebase.stop()
                wait(1000)
                self.drivebase.straight(-60)
                wait(500)
                break
        wait(500) 


    def ir_mapping(self):
        self.lever_motor.run_angle(80, 90)
        self.lever_motor.reset_angle(0)

        for i in range(90):

            self.ev3.screen.draw_circle(87, 123, 4, True, Color.GREEN)    

            lever_angle = self.lever_motor.angle()
            if lever_angle <= -170:
                break
                                
            self.lever_motor.run_angle(80, -5, wait=True)

            print("i =", i)
            print("motor angle =", self.lever_motor.angle())
            print("-------------------------------------------------")
            wait(1000)


    def mapping(self):
        x1 = 10
        y1 = 10
        x2 = 0
        y2 = 0
        d = 0

        self.ev3.screen.draw_box(2, 2, 175, 125) #draw borders
        
        #draws a green point at initial position
        self.ev3.screen.draw_circle(x1, y1, 4, True, Color.GREEN)
        wait(2000)

        #1
        self.drive_until_collision()
        wait(500)

        d = self.drivebase.distance()/10
        wait(2000)

        x2 = x1
        y2 += d 
        self.ev3.screen.draw_line(x1, y1, x2, y2, 3)
        wait(1000)

        #2
        self.drivebase.turn(-90)
        self.drivebase.reset()
        self.drive_until_collision()
        wait(1000)

        d = self.drivebase.distance()/10
        y1 = y2
        x2 += d
        self.ev3.screen.draw_line(x1, y1, x2, y2, 3)

        #3
        self.drivebase.turn(90)
        self.drivebase.reset()
        self.drive_until_collision()
        wait(1000)

        d = self.drivebase.distance()/10
        x1 = x2
        y1 = y2
        y2 += d
        self.ev3.screen.draw_line(x1, y1, x2, y2, 3)

        #4
        self.drivebase.turn(-90)
        self.drivebase.reset()
        self.drive_until_collision()
        wait(1000)

        d = self.drivebase.distance()/10
        y1 = y2
        x1 = x2
        x2 += d
        self.ev3.screen.draw_line(x1, y1, x2, y2, 3)

        #5
        self.drivebase.turn(-90)
        self.drivebase.reset()
        self.drive_until_collision()
        wait(1000)

        d = self.drivebase.distance()/10
        y1 = y2
        x1 = x2
        y2 -= d
        self.ev3.screen.draw_line(x1, y1, x2, y2, 3)
        
        #6
        self.drivebase.turn(90)
        self.drivebase.reset()
        self.drive_until_collision()
        wait(1000)

        d = self.drivebase.distance()/10
        y1 = y2
        x1 = x2
        x2 += d
        self.ev3.screen.draw_line(x1, y1, x2, y2, 3)

        #7
        self.drivebase.turn(90)
        self.drivebase.reset()
        self.drive_until_collision()
        wait(1000)

        d = self.drivebase.distance()/10
        y1 = y2
        x1 = x2
        y2 += d
        self.ev3.screen.draw_line(x1, y1, x2, y2, 3)
        self.ev3.screen.draw_circle(x2, y2, 4, True, Color.RED)
        wait(10000)

        x1 = x2
        y1 = y2
        self.ev3.screen.clear()
        self.ev3.screen.print(x1, y1)
    