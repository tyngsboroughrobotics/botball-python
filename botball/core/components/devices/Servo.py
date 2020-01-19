from botball import wallaby
from ..Component import Component
from ...helpers.scale import scale 


class Servo(Component):
    """ 
    Represents a servo connected to the robot.
    """

    def enable(self): 
        """ 
        Enables the servo. 
        """ 
        wallaby.enable_servo(self.port)

    def disable(self): 
        """ 
        Disables the servo.
        """
        wallaby.disable_servo(self.port)

    def set_position_to(self, position: float):
        """ 
        Sets the servo position and blocks until finished.

        - `position`: A value between 0.0 (leftmost position) and 1
        (rightmost position).
        """

        self.enable()

        # Limit the servo range to within safe boundaries
        bounded_position = int(scale(position, 0, 1, self.min_position, self.max_position))

        # Move the servo
        wallaby.set_servo_position(self.port, bounded_position)

        # just wait a little bit longer for the servo to finish
        wallaby.msleep(100)

        self.disable()

    def position(self) -> float:
        """ 
        The current position of this servo between 0.0 (leftmost) and 1.0
        (rightmost).
        """

        return scale(self.raw_position(), self.min_position, self.max_position, 0, 1)

    def raw_position(self) -> int:
        """
        The current, unbounded position of this servo expressed in raw units.
        """

        return wallaby.get_servo_position(self.port)

    # - Configuration 

    min_position: float = 98
    """
    The minimum position allowed to safely move a servo.

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """

    max_position: float = 1947
    """
    The maximum position allowed to safely move a servo.

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """
