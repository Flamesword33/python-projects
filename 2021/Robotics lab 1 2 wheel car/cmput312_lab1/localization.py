#!/usr/bin/env python3
from math import cos, sin, pi
from ev3dev2.sensor.lego import GyroSensor


class Localization:
    """Localization assume robot begins at [0,0] and facing towards increasing x axis """

    def __init__(self):
        # State is X Y Theta, theta is always in radians
        self.state = {"X": 0.0, "Y": 0.0, "RAD": 0.0}
        self.gyro = self.setup_gyro()
        with open("localization.txt", 'a') as fp:
            print("##### Starting New Log #####")
            print("##### Starting New Log #####", file=fp)

    def log_state(self, action):
        with open("localization.txt", 'a') as fp:
            print('----- Did Action [ {} ]-----'.format(action))
            print('----- Did Action [ {} ]-----'.format(action), file=fp)
            print("{:.5g}, {:.5g}, {:.4g}".format(round(self.state['X']),
                                                  round(self.state['Y']),
                                                  self.radians_to_deg(self.state['RAD'])))
            print("{:.5g}, {:.5g}, {:.4g}".format(self.state['X'],
                                                  self.state['Y'],
                                                  self.radians_to_deg(self.state['RAD'])), file=fp)

    def reset_state(self) -> None:
        """Resets state and gyro"""
        input("Place robot in starting position")
        try:
            self.gyro.reset()
        except:
            pass
        self.state = {"X": 0.0, "Y": 0.0, "RAD": 0.0}

    def get_and_set_heading(self, degrees=False) -> float:
        """
        Set self.state to gyro angle
        """
        self.state['RAD'] = self.deg_to_radians(self.gyro.angle)
        if degrees:
            return self.radians_to_deg(self.state['RAD'])
        else:
            return self.state['RAD']

    def get_heading(self, degrees=False) -> int:
        """
        Get the heading but don't set it
        """
        if degrees:
            return self.radians_to_deg(self.state['RAD'])
        return self.gyro.angle

    def get_state(self) -> str:
        """
        Returns state with heading in degrees in a string
        """
        state = "X: {} Y: {} Heading : {}".format(self.state['X'],
                                                  self.state['Y'],
                                                  (self.radians_to_deg(self.state['RAD']) % 360))
        return state

    def add_rotation(self, rotation: int, is_clockwise: bool) -> None:
        """
        @rotation: rotation in degrees (converted to radians)
        """
        initial_heading = self.state['RAD']
        rotation = self.deg_to_radians(rotation)
        if is_clockwise:
            self.state['RAD'] = (self.state['RAD'] - rotation)
        else:
            self.state['RAD'] = (self.state['RAD'] + rotation)
        self.log_state("Rotates {} degrees CW {} from initial heading {}".format(rotation, is_clockwise, initial_heading))

    def add_line(self, length: int) -> None:
        # Add line to localization, use last known heading
        self.state['X'] += length * (cos(self.state['RAD']))  # cos gives x
        self.state['Y'] += length * (sin(self.state['RAD']))  # sin gives y
        self.log_state(action="Line for length {} at heading {}".format(length, self.state['RAD']))
        # Update new heading
        # If we wanted to could use gyro for more accuracy, but heading should only deviate by a couple degrees
        # self.get_and_set_heading()

    def add_circle(self, degrees, radius, center_point_y, center_point_x, is_clockwise) -> None:
        # Credit: add_circle math for position found
        # https://math.stackexchange.com/questions/311555/how-to-calculate-the-position-of-a-turning-object-based-on-its-rotation
        """Drive in circle starting at last known heading and position"""
        radians = self.deg_to_radians(degrees)
        self.state['X'] = (center_point_x * self.state['X'] - radius * sin(radians))
        self.state['Y'] = (center_point_y * self.state['Y'] + radius * cos(radians))
        self.log_state(action="CW {} Arc for {} degrees at {} radius center X: {} Y: {} Starting at heading {}".format(is_clockwise, degrees, radius, center_point_x, center_point_y, self.state['RAD']))
        # Update new heading
        self.add_rotation(rotation=degrees, is_clockwise=is_clockwise)

    def update_localization(self, time: int, left_ticks: int, right_ticks: int, odometry, l_power, r_power):
        """
        Credit: A Simpler Formula for Dead Recoking
        http://rossum.sourceforge.net/papers/DiffSteer/
        """
        l_distance, v_l = odometry.get_distance_and_velocity(delta_ticks=left_ticks, time=time)
        r_distance, v_r = odometry.get_distance_and_velocity(delta_ticks=right_ticks, time=time)
        v = (v_l + v_r) / 2
        w = (v_r - v_l) / odometry.tire_dist
        theta_t = time * w

        if l_power == r_power:
            "If powers are the same, we can more accurately use just a line"
            self.add_line(length=((l_distance+r_distance)/2))
        else:
            x = v * cos(w)
            y = v * sin(w)
            self.state['X'] += x
            self.state['Y'] += y
            self.state['RAD'] += theta_t
            self.log_state(action="L {}: R {}: T: {}".format(l_power, r_power, time))

    @staticmethod
    def setup_gyro():
        """Setup and Calibrates gyro, try and except so I can test when not connected to robot"""
        try:
            gyro = GyroSensor()
            input("Setting up GYRO, please keep robot still and hit Enter to continue")
            gyro.calibrate()
            gyro.reset()
            print("Gyro Calibration Complete")
            return gyro
        except:
            print("Gyro Not Found")

    @staticmethod
    def deg_to_radians(degrees):
        return degrees * pi / 180

    @staticmethod
    def radians_to_deg(radians):
        return radians * 180 / pi

    def localization_test(self):
        def assertion(test):
            try:
                assert (self.state['X'] + self.state['Y'] < 0.1)
            except:
                print("{} ERROR: X&Y location wrong".format(test))
            try:
                assert (self.radians_to_deg(self.state['RAD']) % 360 < 0.1)
            except:
                print("{} ERROR: Radians wrong".format(test))
            self.reset_state()
        # Set of tests to make sure localization is working in theory, not using motors

        # Do a square above x axis
        for i in range(4):
            self.add_line(length=100)
            self.add_rotation(rotation=90, is_clockwise=False)
        assertion('square')

        # Do a rectangle above x axis
        rect = [100, 50]
        for i in range(4):
            self.add_line(length=rect[i % 2])
            self.add_rotation(rotation=90, is_clockwise=False)
        assertion('rectangle')

        # Do a diamond below the x axis
        self.add_rotation(rotation=45, is_clockwise=True)
        for i in range(4):
            self.add_line(length=100)
            self.add_rotation(rotation=90, is_clockwise=True)
        self.add_rotation(rotation=45, is_clockwise=True)
        assertion('diamond')

        # Do a circle
        self.add_line(length=100)
        self.add_rotation(rotation=90, is_clockwise=False)
        self.add_circle(degrees=360, radius=100, center_point_x=0, center_point_y=0, is_clockwise=False)
