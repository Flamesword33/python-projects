#!/usr/bin/env python3
import time
from math import pi, sin, cos
from ev3dev2.wheel import Wheel


class OurWheel(Wheel):
    def __init__(self):
        Wheel.__init__(self, 55, 29)


class Odometry:

    @staticmethod
    #TODO Not used, if Nathan does not use, delete
    def inst_vel(icc, w) -> int:
        return round(icc * w)

    def __init__(self, robot, tire_dist=16.75, wheel_circ=17.5):
        self.tire_dist = tire_dist
        self.wheel_circ = wheel_circ
        self.max_dps = 1050
        self.power_to_dps = 0.01 * self.max_dps
        self.tank_drive = robot.tank_drive

    def move_straight_line(self, distance: int, power: int):
        """
        Calculates the rotations needed to move a given distance in cm
        """
        rotations = distance / self.wheel_circ
        self.tank_drive.on_for_rotations(power, power, rotations)

    def get_distance_and_velocity(self, delta_ticks: int, time: int):
        """Gets distance traveled and velocity of wheel based on delta ticks"""
        wheel_rotations = delta_ticks/360
        distance = wheel_rotations * self.wheel_circ
        velocity = distance / time
        return distance, velocity

    #reading your github comment, added abs to work for either rotation
    # TODO Used by Nathan if not getting used remove
    def get_radius(self, v_l, v_r):
        """Get radius of icc in cm"""
        if v_r - v_l == 0:
            return 0
        radius = abs((self.tire_dist/2) * (v_r + v_l) / (v_r - v_l))
        return round(radius)

    #get_angle_per_second is a reskin of get_delta_angle
    #because I couldn't remember what it was called while typing code.
    # TODO Used by Nathan if not getting used remove
    def get_angle_per_second(self, left_velocity, right_velocity):
        """Return W in radian"""
        angle_per_second = (right_velocity - left_velocity)/self.tire_dist
        return round(angle_per_second)

    ##NEED THIS, PLEASE DONT REMOVE##
    # TODO Used by Nathan if not getting used remove
    def get_icc(self, radius, heading, is_clockwise):
        if is_clockwise:
            icc = [radius * sin(heading), (-1 * radius * cos(heading))]
        else:
            icc = [(-1 * radius * sin(heading)), radius * cos(heading)]
        return icc

    @staticmethod
    def deg_to_radians(degrees):
        return degrees * pi / 180

    @staticmethod
    def radians_to_deg(radians):
        return radians * 180 / pi


