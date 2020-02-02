from .. import bindings
from .Movable import Movable
from ..helpers import Direction

class Motor(Movable): 
    """
    Represents a motor connected to the robot.
    """ 

    def __copy__(self):
        return Motor(self.port, self.speed)

    def move(self, direction: Direction, mm: float, block: bool = True, sleep: bool = True):
        """ 
        Moves the motor.

        - `direction`: The direction in which to move the motor.

        - `mm`: The distance to move the motor in mm.

        - `block`: Whether to block the thread until finished. If you don't
        block the thread, you are responsible for calling `off()` on the
        motor!

        - `sleep`: Whether to sleep for `Motor.default_sleep_time()` ms after
        the motor finishes driving. You should probably keep this set to
        `True` unless you sleep somewhere else in the program, because not
        sleeping will cause the motor to sometimes finish too early and make
        future movements unreliable (not fun to debug!). If this is set to
        `False`, then the value of `mm` is ignored.
        """

        ticks = int(self.speed * self.max_ticks)
        bindings.move_at_velocity(self.port, ticks * direction.multiplier())

        if block:
            ms_to_sleep = int(self._secs_to_sleep_for_distance(mm, ticks) * 1000)

            bindings.msleep(ms_to_sleep)
            bindings.off(self.port)

        if sleep:
            bindings.msleep(self.default_sleep_time)

    # - Constants

    default_sleep_time: int = 0
    """
    The amount of time (in milliseconds) to allow the motors to sleep for in 
    between movements. This allows the motor a bit of time to stop moving before
    the next motor is sent.

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """

    # - Calculation

    max_ticks = 1500
    secs_it_takes_to_travel_100_mm_at_max_ticks = 0.5275

    def _secs_to_sleep_for_distance(self, distance_in_mm, ticks):
        return(self.max_ticks * self.secs_it_takes_to_travel_100_mm_at_max_ticks * distance_in_mm) / (100 * ticks)
