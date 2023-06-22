#!/usr/env/python3

class Outputs():
    def __init__(self, **kwargs):
        self.name = "Outputs"
        self.outputs = kwargs
    
    def __str__(self):
        string =  f'[{self.name}]\n'
        for key, value in self.outputs.items():
            string += f'{key}={value}\n'
    
        string += '[]\n'
        return string
