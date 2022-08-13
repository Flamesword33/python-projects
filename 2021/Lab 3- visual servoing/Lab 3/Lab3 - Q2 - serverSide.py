#!/usr/bin/python

"""Lab 3 - Q2 - serverSide"""
## October 25, 2021
## Nathan Pelletier
## Joshua Jarman

import sys
from math import sin, pi, asin, acos, atan2, sqrt
from ev3dev2 import motor
import server
import color_tracking
import time

###########
##GLOBALS##
CurrentPosition = [0,0] #current position in degrees

Motor = motor.LargeMotor
OUTPUT_A = motor.OUTPUT_A
OUTPUT_B = motor.OUTPUT_B



def debug_print(*args, **kwargs):
    """Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    """
    print(*args, **kwargs, file=sys.stderr)

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

    angle1 = theta1*180/pi
    angle2 = theta2*180/pi

    server.sendAngles(str(angle1) + " " + str(angle2))

def initialJacobian(angle1, angle2, x, y):
    """Makes a simple (and wrong) initial jacobian
    @angle1: first joint angle of robot
    @angle2: second joint angle of robot
    @x: observed change in x
    @y: observed change in y
    @return: a 2x2 matrix jacobian, angle * jacobian = position"""
    jacobian = [[x/angle1, y/angle1],[x/angle2, y/angle2]]
    return jacobian

def updateJacobian(jacobian, observedPosition, inputedAngles):
    """Updates jacobian via error analysis
    Formula used: Broyden Update 
        J+1 = J + (position - J * angles)/(angles^2) 

    @jacobian: a 2x2 matrix conatining information for angle * jacobian = position
    @observedPosition: a 2 element array containing the observed x and y from moving the machine
    @inputedAngles: a 2 element array containing the inputed angles
    @return: 2x2 matrix, updated jacobian"""
    tempArray = [0,0]
    tempMatrix = [[0,0],[0,0]]
    divisor = inputedAngles[0]**2 + inputedAngles[1]**2
    for i in range(2):
        tempArray[i] = (jacobian[i][0] * inputedAngles[0])
        tempArray[i] += (jacobian[i][1] * inputedAngles[1])
        tempArray[i] = observedPosition[i] - tempArray[i]
    for j in range(2):
        for k in range(2):
            tempMatrix[j][k] = tempArray[j] * inputedAngles[k]
            tempMatrix[j][k] = tempMatrix[j][k]/divisor
            jacobian[j][k] = jacobian[j][k] + tempMatrix[j][k]
    return jacobian

def invertmatrix(matrix):
    """takes a 2x2 matrix and inverts it
    @matrix: 2x2 matrix"""
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    determinate = a*d - b*c
    invertedMatrix = [[d/determinate, -1*b/determinate],
                      [-1*c/determinate, a/determinate]]
    return invertedMatrix

def positionToAngle(jacobian, position):
    """Inverts a Jacobian and matrix multiplies it by the provided postions
    @jacobian: 2x2 matrix, turns angles to postion vectors
    @position: [x,y] vector to convert to angles
    @return: [angle1, angle2]"""
    invJ = invertmatrix(jacobian)
    angle1 = (invJ[0][0] * position[0]) + (invJ[0][1] * position[1])
    angle2 = (invJ[1][0] * position[0]) + (invJ[1][1] * position[1])
    return [angle1, angle2]

def angleToPosition(jacobian, angles):
    """Takes a Jacobian and matrix multiplies it by the provided angles
    @jacobian: 2x2 matrix, turns angles to postion vectors
    @position: [angle1, angle2] vector to convert to coordinates
    @return: [x, y]"""
    x = (jacobian[0][0] * angles[0]) + (jacobian[0][1] * angles[1])
    y = (jacobian[1][0] * angles[0]) + (jacobian[1][1] * angles[1])
    return [x, y]

def wiggle(Server, tracker):
    """Wiggles the arm alowing us to find our initial jacobian.
    Must wiggle one joint at a time.
    @Server: object refering to server class
    @tracker: object refering to tracker class
    @return: Jacobian 2x2 matrix of form Jacobian * angles = position"""
    Server.sendAngles("10 0")
    current = tracker.point
    jacobian = initialJacobian(10, 0, current[0], current[1])
    j1 = jacobian[0][0]
    j2 = jacobian[1][0]
    Server.sendAngles("0 10")
    current = tracker.point
    jacobian = initialJacobian(0, 10, current[0], current[1])
    jacobian[0][0] = j1
    jacobian[1][0] = j2
    return jacobian

def averageOutGoal(counter, tracker, totalGoal):
    """Takes average of all goal points to smooth out noise.
    @counter: int counter
    @tracker: object refering to Tracker class
    @totalGoal: Total sum of all goals coordinates given by visual servo so far"""
    goal = [0,0,0]
    if counter < 100:
        goal = tracker.goal
        totalGoal[0] += goal[0]
        totalGoal[1] += goal[1]
        goal[0] = totalGoal[0]/counter
        goal[1] = totalGoal[1]/counter
        counter += 1
        return goal
    goal = tracker.goal
    goal[0] = totalGoal[0]/counter
    goal[1] = totalGoal[1]/counter
    return goal

def main():
    host = "192.168.0.2"
    port = 9999
    s = server.Server(host, port)
    tracker = color_tracking.Tracker('b', 'r')

    angles = [10,10]
    totalGoal = [0,0,0]
    counter = 1

    jacobian = wiggle(s, tracker)
    current = tracker.point
    goal = tracker.goal
    
    # should stop at + or - 25 
    while abs(current[0] - goal[0]) > 25 and abs(current[0] - goal[0]) > 25:
        current = tracker.point
        goal = averageOutGoal(counter, tracker, totalGoal)
        jacobian = updateJacobian(jacobian, current, angles)

        print("Point is at: "+str(current))
        print("Goal is at: "+str(goal))

        angles = positionToAngle(jacobian, [goal[0], goal[1]])
        s.sendAngles(str(angles[0]) + " " + str(angles[1]))
        
        time.sleep(2)

main()