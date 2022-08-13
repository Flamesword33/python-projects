#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_D, MoveDifferential, SpeedRPM, MoveTank, LargeMotor
from localization import Localization
from behaviours import Behaviours
from odometry import Odometry, OurWheel
from testing import Tests
import signal
from math import pi, sqrt


class Robot:

    def __init__(self, tire_distance=16.75, wheel_circ=17.5, diff_drive_distance=153):
        # Setup Motors
        self.left_motor = LargeMotor(OUTPUT_D)
        self.right_motor = LargeMotor(OUTPUT_B)
        self.tank_drive = MoveTank(OUTPUT_D, OUTPUT_B)
        self.diff_drive = MoveDifferential(OUTPUT_D, OUTPUT_B, OurWheel, diff_drive_distance)
        self.normal_speed = 30

        # Robot variables
        self.localization = Localization()
        self.odometry = Odometry(self, wheel_circ=wheel_circ, tire_dist=tire_distance)
        self.diff_drive.gyro = self.localization.gyro
        self.behaviours = Behaviours(self)
        self.tests = Tests(self)

        # Kill motors on sigterm
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        """Kills motors on sigterm/sigint"""
        self.tank_drive.stop()
        exit(78)


    def do_movement(self, rectangle=False, lemn=False, line=False, circle=False):
        """
        #3) Write a program that receives as input one of the following four shapes and performs the desired movement
        """
        if rectangle:
            self.rectangle_movement()
        if lemn:
            self.infinity_movement(radius=10)
        if line:
            self.line_movement(20, self.normal_speed)
        if circle:
            self.circle_movement(radius=10, degrees=360, is_clockwise=False)

    def rotate(self, degrees: int, is_clockwise=True, speed=SpeedRPM(20), use_gyro=True, use_diff_drive=True) -> None:
        """
        @degrees: degrees to turn, always positive
        @is_clockwise: if True rotates clockwise, if False rotates counter clockwise
        Defaults to clockwise rotation with speed 20 for more accuracy
        """
        if use_diff_drive:
            if is_clockwise:
                self.diff_drive.turn_right(speed=speed, degrees=degrees, use_gyro=use_gyro)
            else:
                self.diff_drive.turn_left(speed=speed, degrees=degrees, use_gyro=use_gyro)
            self.localization.add_rotation(rotation=degrees, is_clockwise=True)
        else:
            # TODO Add manual rotation, not needed though
            pass

    def rectangle_movement(self, width=30, height=10) -> None:
        """
        Moves in a rectangle counter clockwise starting at the bottom left corner
        @width: width in cm
        @height: height in cm
        """
        for i in range(2):
            self.line_movement(distance=width, power=self.normal_speed)
            self.rotate(degrees=90, is_clockwise=False)
            self.line_movement(distance=height, power=self.normal_speed)
            self.rotate(degrees=90, is_clockwise=False)

    def line_movement(self, distance: int, power: int, use_diff_drive=True) -> None:
        """
        @distance: distance in cm
        @power: power on a scale from 0->100
        Moves in a straight line for given distance
        """
        self.odometry.move_straight_line(distance, power)
        self.localization.add_line(distance)

    def circle_movement(self, radius: int, degrees: int, is_clockwise: bool, use_diff_drive=True) -> None:
        """
        Does a circle
        @radius: of circle in cm
        @degrees: how many degrees of rotation
        """
        if use_diff_drive:
            radius *= 10  # convert cm to mm
            circumference = radius * 2 * pi
            circ_ratio = degrees/360

            if is_clockwise:
                self.diff_drive.on_arc_right(SpeedRPM(self.normal_speed), radius, circumference * circ_ratio)
            else:
                self.diff_drive.on_arc_left(SpeedRPM(self.normal_speed), radius, circumference * circ_ratio)

            # Update Localization
            #center_point = self.odometry.get_icc(radius, heading, is_clockwise)
            #self.localization.add_circle(degrees, radius, center_point[0], center_point[1], is_clockwise)
        else:
            # TODO Add manual circle, not needed though
            pass

    def infinity_movement(self, radius: int) -> None:
        """
        @radius: radius of half circle in infinity symbol
        """
        line_length = sqrt(2 * radius * radius)
        self.circle_movement(radius=radius, degrees=180, is_clockwise=True)
        self.rotate(degrees=45, is_clockwise=True)
        self.line_movement(distance=line_length*2, power=self.normal_speed, use_diff_drive=True)
        self.rotate(degrees=45, is_clockwise=False)
        self.circle_movement(radius=radius, degrees=180, is_clockwise=False)
        self.rotate(degrees=45, is_clockwise=False)
        self.line_movement(distance=line_length*2, power=self.normal_speed, use_diff_drive=True)
        self.rotate(degrees=45, is_clockwise=True)

    def complex_driving_instructions(self, command) -> None:
        """
        Drives a series of commands in matrix form
        [left wheel power, right wheel power, time]
        """
        for rows in range(len(command)):
            left_start = self.left_motor.position
            right_start = self.right_motor.position
            # TODO off by ~20cm for x and y, could do the divide and conquer method
            self.tank_drive.on_for_seconds(command[rows][0],
                                           command[rows][1],
                                           command[rows][2])
            left_ticks = self.left_motor.position-left_start
            right_ticks = self.right_motor.position-right_start
            self.localization.update_localization(time=command[rows][2],
                                                  left_ticks=left_ticks,
                                                  right_ticks=right_ticks,
                                                  odometry=self.odometry,
                                                  l_power=command[rows][0],
                                                  r_power=command[rows][1])


if __name__ == "__main__":
    robot = Robot()
    # instructions = [[80, 60, 2], [60, 60, 1], [-50, 60, 4]]
    # # Do a circle
    # #instructions = [[30, 50, 10]]
    # robot.complex_driving_instructions(command=instructions)
    # print(robot.localization.get_state())
    #robot.behaviours.aggression()
    #sleep(1)
   # robot.behaviours.cowardice()
    #sleep(1)
    robot.behaviours.love()
