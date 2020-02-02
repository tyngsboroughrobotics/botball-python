import time
from .. import bindings
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
        bindings.enable_servo(self.port)

    def disable(self): 
        """ 
        Disables the servo.
        """
        bindings.disable_servo(self.port)

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
        bindings.set_servo_position(self.port, bounded_position)
        
        # Wait for the servo to finish
        time.sleep(self.servo_sleep_amount)

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

    servo_sleep_amount = 0.75
    """
    The number of seconds to sleep between servo movements. Setting this to 0
    causes the `Servo.set_position_to` method to return immediately.

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """
