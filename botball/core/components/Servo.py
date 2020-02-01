from ... import wallaby
from .Component import Component
from ..helpers import scale


class Servo(Component):
    """ 
    Represents a servo connected to the robot.
    """ 

    _position: int = 0 

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

        # Move the servo to the bounded position
        wallaby.set_servo_position(self.port, bounded_position)
        
        # Wait for the servo to finish
        wallaby.msleep(int(100 + abs(self._position - bounded_position) * self.ms_per_tick))

        self._position = bounded_position

        self.disable()

    def position(self) -> float:
        """ 
        The current position of this servo between 0.0 (leftmost) and 1.0
        (rightmost).
        """

        return scale(self._position, self.min_position, self.max_position, 0, 1)

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

    ms_per_tick: float = 1.6
    """
    The number of milliseconds it takes for the servo to move one tick.

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """
