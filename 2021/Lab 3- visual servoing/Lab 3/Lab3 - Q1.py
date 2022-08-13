#!/usr/bin/python

"""Lab 3 - Q1"""
## October 25, 2021
## Nathan Pelletier
## Joshua Jarman

import sys
from math import sin, cos, pi, asin, acos, atan, atan2, sqrt
from ev3dev2 import motor
import time

###########
##GLOBALS##
CurrentAngles = [0,0] #current position in degrees

Motor = motor.LargeMotor
OUTPUT_A = motor.OUTPUT_A
OUTPUT_B = motor.OUTPUT_B

def debug_print(*args, **kwargs):
    """Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    """
    print(*args, **kwargs, file=sys.stderr)

def moveArm(theta1, theta2):
    """Moves motors to desired position, requires calibration with the bot"""
    Motor.on_for_degrees(10, -theta1, brake = False)
    Motor.on_for_degrees(10, -theta2)
    time.sleep(1)

def resetArm():
    Motor.on_for_degrees(10, CurrentAngles[0])
    Motor.on_for_degrees(10, CurrentAngles[1])
    CurrentAngles[0] = 0
    CurrentAngles[1] = 0

def ArmKinInvGeo(x, y):
    """ Takes coordinates and converts them to angles. Sends angles into moveArm
    @x: horizontal position in cm
    @y: vertical position in cm"""
    stdLength = 8
    L1 = (stdLength * 14)/10  # length of first arm
    L2 = (stdLength * 10)/10  # length of second arm

    theta2 = acos((x*x + y*y - L1*L1 - L2*L2) / (2*L1*L2))
    theta2 = abs(theta2)

    theta1 = -abs(asin((L2*sin(theta2)) / (sqrt(x*x + y*y)))) + atan2(y,x)

    angle1 = theta1*180/3.141592654
    angle2 = theta2*180/3.141592654

    moveArm(angle1 - CurrentAngles[0], angle2 - CurrentAngles[1])
    CurrentAngles[0] = angle1
    CurrentAngles[1] = angle2


def drawLine(point1, point2):
    """Given two coordinates drives in a line between them in ten steps
    @return: a garbo number to kill the program early in the case of division by 0"""

    ArmKinInvGeo(point1[0], point1[1])
    if (point2[0]- point1[0] == 0):
        verticalLine(point1, point2)
        return 0
    elif (point2[1]- point1[1] == 0):
        horizontalLine(point1, point2)
        return 0
    slope = (point2[1] - point1[1])/(point2[0] - point1[0])
    b = point2[1] - slope*point2[0]
    stepSize = (point2[0] - point1[0])/10
    for i in range(1, 11):
        tempX = point1[0] + stepSize * i
        tempY = slope*tempX + b
        ArmKinInvGeo(tempX, tempY)
    return 0

def verticalLine(point1, point2):
    stepSize = (point2[1] - point1[1])/10
    for h in range(1, 11):
        ArmKinInvGeo(point1[0], h * stepSize + point1[1])

def horizontalLine(point1, point2):
    stepSize = (point2[0] - point1[0])/10
    for i in range(1, 11):
        ArmKinInvGeo(i * stepSize + point1[0], point1[1])

def drawLine2(point, angle, distance):
    """Variant of driveInLine, uses point, angle and distance"""
    point2 = [0,0]
    rad = (angle * pi)/180
    point2[0] = point[0] + distance*sin(rad)
    point2[1] = point[1] + distance*cos(rad)
    drawLine(point, point2)

def drawArc(matrixPoints):
    for point in matrixPoints:
        ArmKinInvGeo(point[0], point[1])

if __name__ == "__main__":
    drawLine([15,7],[2,3])
    resetArm()
    drawLine2([5,8], 25, 10)
    resetArm()
    # unsure of optional question 1 c) draw an arc defined by n points
    # 3 points form a calculatable arc. (start, radius, end)
