"""
This is the Robot class
"""

class Robot:
    
    def __init__(self, MovementControl, MovementObjectControl, Camera, System, Engine) -> None:
        self._MovementControl = MovementControl
        self._MovementObjectControl = MovementObjectControl
        self._Camera = Camera
        self._System = System
        self._Engine = Engine
        

    