import libwallaby
from ..Movable import Movable
from ..Direction import Direction
from ...helpers.scale import scale 


class Servo(Movable):
    """ 
    Represents a servo connected to the robot.
    """ 

    _position: int = 0 

    def enable(self): 
        """ 
        Enables the servo. 
        """ 
        libwallaby.enable_servo(self.port)

    def disable(self): 
        """ 
        Disables the servo.
        """
        libwallaby.disable_servo(self.port) 

    def set_position_to(self, position: float):
        """ 
        Sets the servo position and blocks until finished.

        - `position`: A value between 0.0 (leftmost position) and 1
        (rightmost position).
        """

        initial_position = self._position 

        # Limit the servo range to within safe boundaries
        bounded_position = scale(position, 0, 1, self.min_position, self.max_position)

        # Calculate how far the servo actually needs to travel
        difference = bounded_position - initial_position
        direction = Direction.Forward if difference >= 0 else Direction.Backward
        total_distance = abs(difference)
        time_interval = self._time_interval()

        x = 0 
        while x < total_distance:
            self._position = x 

            raw_position = initial_position + (x * direction.multiplier())
            libwallaby.set_servo_position(self.port, raw_position)

            libwallaby.msleep(time_interval)
            x += 1
        
        # just wait a little bit longer for the servo to finish
        libwallaby.msleep(100)

        self.disable()

    def position(self) -> float:
        """ 
        The current position of this servo between 0.0 (leftmost) and 1.0
        (rightmost).
        """

        return scale(self._position, self.min_position, self.max_position, 0, 1)

    # - Configuration 

    min_position: float = 300 
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

    # - Calculation

    def _time_interval(self) -> int:
        """
        Returns the amount of time (in ms) that should be spent between each 
        increment of the servo position, based on the servo's speed.
        """
        return int((1.0 - self.speed) * 5)
