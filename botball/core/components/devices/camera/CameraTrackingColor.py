from ....helpers.enum import Enum


class CameraTrackingColor(Enum):
    """
    Represents the available colors of objects to camera can track. Each color
    has a corresponding configuration file in the robot.
    """

    Red = "red"
    Yellow = "yellow"
    Green = "green"

    def __str__(self):
        return self.value
