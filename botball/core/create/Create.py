from botball import libwallaby
from ..components import Direction, Motor
from ..helpers import scale


# noinspection PyMethodMayBeStatic
class Create(object):
    """
    Represents a controller connected to an iRobot Create robot.
    """

    speed: float 
    """
    The speed of the Create between 0.0 (slowest) and 1.0 (fastest).
    """

    def __init__(self, speed: float):
        """
        Initializes the Create and blocks until a connection is established. The
        Create should only be used inside a `with` statement; for example:

        >>> with Create(speed=1.0) as create:
        ...     create.drive(Direction.Forward, mm=100)

        - **Warning:** If the controller is not connected to a Create or the
        Create is not turned on, then the program will freeze indefinitely.
        """
        self.speed = speed

    def __enter__(self):
        libwallaby.create_connect()
        libwallaby.msleep(1500)  # wait for the connection to finish establishing

    def __exit__(self, exception_type, exception_value, traceback):
        libwallaby.create_disconnect()

    # - Driving

    def drive(self, direction: Direction, mm: int, block: bool = True, sleep: bool = True):
        """
        Drives the Create.

        - `direction`: The direction in which to move.

        - `mm`: The distance to move in mm.

        See `Motor.move()` for information on the other parameters. 
        """
        ticks = scale(self.speed, 0, 1, 0, self.max_speed) \
            * direction.multiplier()

        libwallaby.create_drive_straight(int(ticks))

        if not block:
            return

        def current_distance():
            return libwallaby.get_create_distance()

        target_distance = current_distance() + (mm * direction.multiplier())

        # Stop the Create once the current distance is ±2 mm from the target

        def within_target_distance() -> bool:
            return target_distance - 2 <= current_distance() <= target_distance + 2

        while not within_target_distance():
            libwallaby.msleep(5)

        if sleep:
            libwallaby.msleep(Motor.default_sleep_time)

    def stop(self):
        """
        Stops the Create if it is moving.
        """
        libwallaby.create_stop()

    # - Constants

    max_speed: float = 500.0
    """
    The fastest Create speed in mm/sec.

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """
