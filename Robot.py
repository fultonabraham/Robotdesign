"""
This is the Robot class
"""

class Robot:
    
    def __init__(self, MovementControl, ArmControl, Camera, System, Engine) -> None:
        self._MovementControl = MovementControl
        self._ArmControl = ArmControl
        self._Camera = Camera
        self._System = System
        self._Engine = Engine
        

    