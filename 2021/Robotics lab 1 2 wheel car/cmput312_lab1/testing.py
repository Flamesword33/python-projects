#!/usr/bin/env python3
from math import atan, pi
import time
from ev3dev2.motor import SpeedRPM


class Tests:

    def __init__(self, robot):
        self.robot = robot

    def power_test(self):
        """
        Test designed to measure variance in distance and degrees when traveling 1 meter at various distances
        """
        self.robot.localization.reset_state()
        with open("motor_tests.txt", 'w') as fp:
            print("##### Line Test #####", file=fp)
            for i in range(10, 110, 10):
                gyro1 = self.robot.localization.get_heading(degrees=True)
                left_start = self.robot.left_motor.position
                right_start = self.robot.right_motor.position
                self.robot.line_movement(distance=100, power=i, use_diff_drive=False)
                left_rotations = self.robot.left_motor.position-left_start
                right_rotations = self.robot.right_motor.position-right_start
                avg_rotations = (left_rotations+right_rotations)/2
                dist_rot = avg_rotations * self.robot.odometry.wheel_circ
                gyro2 = self.robot.localization.get_heading(degrees=True)
                dist = float(input("How far did the robot travel in cm? "))
                yaw = float(input("How far did the robot rotate in cm? "))
                print("Power {:3} - Actual Distance traveled: {:3}  Error: {:2} - Encoder Distance traveled {:5}  Error: {:2} ".format(i, dist, abs(100-dist), dist_rot, abs(100-dist_rot) ))
                print("Power {:3} - Actual Distance traveled: {:3}  Error: {:2} - Encoder Distance traveled {:5}  Error: {:2} ".format(i, dist, abs(100-dist), dist_rot, abs(100-dist_rot) ), file=fp)
                print("Power {:3} - Start Heading: {:2} End Heading: {:2} Gyro Diff: {:2} Measured Diff: {:.3g}".format(i, gyro1, gyro2, abs(gyro1-gyro2), atan(yaw/dist)*180/pi))
                print("Power {:3} - Start Heading: {:2} End Heading: {:2} Gyro Diff: {:2} Measured Diff: {:.3g}".format(i, gyro1, gyro2, abs(gyro1-gyro2), atan(yaw/dist)*180/pi), file=fp)
                input("Continue?")

    def rotation_test(self):
        """Test designed to measure variance in distance and degrees"""
        with open("rotation_tests.txt", 'w') as fp:
            print("##### Rotation Test #####", file=fp)
            for i in range(10, 110, 20):
                self.robot.localization.gyro.reset()
                gyro1 = self.robot.localization.get_heading()
                self.robot.rotate(degrees=360, use_gyro=False, speed = SpeedRPM(i))
                gyro2 = self.robot.localization.get_heading()
                rotation_diff = float(input("How many degrees was the rotation off? "))
                print("Power {:3} - Start Heading: {:2} End Heading: {:2} Gyro Diff: {:2} Measured Diff: {:.3g}".format(i, gyro1, gyro2, abs(360-gyro2-gyro1), rotation_diff))
                print("Power {:3} - Start Heading: {:2} End Heading: {:2} Gyro Diff: {:2} Measured Diff: {:.3g}".format(i, gyro1, gyro2, abs(360-gyro2-gyro1), rotation_diff), file=fp)

    def get_dps(self):
        """
        Calculate DPS using encoders, how badly off are these from our estimates of POWER * 0.01 * 1050
        TLDR: Our estimate cannot be trusted for powers > 70
        """
        with open("dps_tests.txt", 'w') as fp:
            for i in range(10, 110, 10):
                left_start = self.robot.left_motor.position
                right_start = self.robot.right_motor.position
                self.robot.tank_drive.on_for_seconds(i, i, 1)
                time.sleep(0.5)
                left_ticks = (self.robot.left_motor.position-left_start)
                right_ticks = (self.robot.right_motor.position-right_start)
                print("Power {} - Left DPS={} Right DPS={} Estimate DPS {:.4g}".format(i, left_ticks, right_ticks, i*self.robot.odometry.power_to_dps))
                print("Power {} - Left DPS={} Right DPS={} Estimate DPS {:.4g}".format(i, left_ticks, right_ticks, i*self.robot.odometry.power_to_dps), file=fp)

    def dead_recon_test(self):
        pass

