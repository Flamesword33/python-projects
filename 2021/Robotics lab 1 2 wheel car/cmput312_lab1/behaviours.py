#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_4, INPUT_3
from ev3dev2.button import Button


class Behaviours:

    def __init__(self, robot):
        self.robot = robot
        self.light_sensor_l = ColorSensor(INPUT_3)
        self.light_sensor_r = ColorSensor(INPUT_4)
        self.button = Button()

    def convert_light_to_motor(self):
        left_sensor = min(100, self.light_sensor_l.ambient_light_intensity * 2)
        right_sensor = min(100, self.light_sensor_r.ambient_light_intensity * 2)
        return left_sensor, right_sensor

    def cowardice(self):
        while self.belly_button_pressed() is False:
            l_pow, r_pow = self.convert_light_to_motor()
            self.robot.tank_drive.on_for_seconds(l_pow, r_pow, 0.25)

    def aggression(self):
        while self.belly_button_pressed() is False:
            l_pow, r_pow = self.convert_light_to_motor()
            self.robot.tank_drive.on_for_seconds(r_pow, l_pow, 0.25)

    def love(self):
        while self.belly_button_pressed() is False:
            l_pow, r_pow = self.convert_light_to_motor()
            self.robot.tank_drive.on_for_seconds(100-r_pow, 100-l_pow, 0.25)

    def belly_button_pressed(self):
        return self.button.any()
