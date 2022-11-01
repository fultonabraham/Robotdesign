"""
This is the MovementControl class
"""

class MovementControl:
    
    def __init__(self, MovementType) -> None:
        self._MovementType = MovementType

    def TurnLeft(self):
        print("Turn the Robot Left")

    
    def TurnRight(self):
        print("Turn the Robot Right")

    
    def Spin(self):
        print("Make the Robot Spin")

   
    def MoveForward(self):
        print("Move the Robot Forward")

    
    def MoveBackwards(self):
        print("Move the Robot Backwards")

    
    
    