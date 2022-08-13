#!/usr/bin/python

"""Lab 3 - Q2 - clientSide"""
## October 25, 2021
## Nathan Pelletier
## Joshua Jarman

from ev3dev2 import motor
from ev3dev2.button import Button
import time
from client import Client

Motor = motor

def moveArm(theta1, theta2):
    """Moves motors to desired position, requires calibration with the bot"""
    Motor.on_for_degrees(10, -theta1, brake = False)
    Motor.on_for_degrees(10, -theta2)

if __name__ == "__main__":
    host = "10.0.0.246"
    port = 9999
    client = Client(host, port)
    previousData = [0,0]

    while Button.any() == False:
        data = client.pollData()
        print(data)
        # We are expecting a string of ints seperated by spaces 
        # "https://www.w3schools.com/python/ref_string_split.asp"
        data.split()
        if previousData[0] != data[0] or previousData[1] != data[1]:
            moveArm(data[0], data[1])
            previousData[0] = data[0]
            previousData[1] = data[1]
        time.sleep(1)