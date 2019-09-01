from botball import wallaby
from ..Movable import Movable
from ..Direction import Direction
from ...helpers.scale import scale 


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
        velocity = int(self._velocity() * direction.multiplier())

        wallaby.move_at_velocity(self.port, velocity)

        if block:
            distance_ticks = self._mm_to_ticks(mm)
            ms_to_sleep = int(self._ticks_to_ms(distance_ticks))

            wallaby.msleep(ms_to_sleep)
            wallaby.off(self.port)

        if sleep:
            wallaby.msleep(self.default_sleep_time)

    # - Constants

    motor_ticks_per_mm: float = 10 / 1.13
    """
    The number of motor "ticks" (`wallaby`'s internal motor unit) in one
    millimeter.

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """

    motor_ticks_per_second: float = 818
    """
    The number of motor "ticks" (`wallaby`'s internal motor unit) a
    motor will travel at full speed in one second.

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """

    default_sleep_time: int = 300 
    """
    The amount of time (in milliseconds) to allow the motors to sleep for in 
    between movements. This allows the motor a bit of time to stop moving before
    the next motor is sent.

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """

    # - Calculation

    def _mm_to_ticks(self, mm: float) -> float:
        return self.motor_ticks_per_mm * mm 
    
    def _velocity(self) -> float:
        return scale(self.speed, 0, 1, 0, self.motor_ticks_per_second)
    
    def _ticks_to_ms(self, ticks: float) -> float:
        return abs(ticks * self.motor_ticks_per_second / self._velocity())
