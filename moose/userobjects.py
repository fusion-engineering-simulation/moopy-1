#!/usr/env/python3

from enum import IntEnum, auto

class UserObjects():
    def __init__(self, **kwargs):
        self.name = "UserObjects"
        self.solve_objects = kwargs

    def __str__(self):
        string =  f'[{self.name}]\n'
        for key in self.solve_objects.keys():
            string += f'{key}="{self.solve_objects[key]}"\n'
        string += '[]\n'
        return string
