from ... import wallaby
from ..components import Motor
from ..helpers import Direction, scale


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
        Initializes the Create and blocks until a connection is established.

        - **Warning:** If the controller is not connected to a Create or the
        Create is not turned on, then the program will freeze indefinitely.
        """
        self.speed = speed

        wallaby.create_connect()
        wallaby.msleep(1500)  # wait for the connection to finish establishing

    def disconnect(self):
        """
        Manually disconnect the Create. This will be done automatically when
        your program finishes running.
        """
        wallaby.create_disconnect()

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

        wallaby.create_drive_straight(int(ticks))

        if not block:
            return

        def current_distance():
            return wallaby.get_create_distance()

        target_distance = current_distance() + (mm * direction.multiplier())

        # Stop the Create once the current distance is ±2 mm from the target

        def within_target_distance() -> bool:
            return target_distance - 2 <= current_distance() <= target_distance + 2

        while not within_target_distance():
            wallaby.msleep(5)

        if sleep:
            wallaby.msleep(Motor.default_sleep_time)

    def stop_moving(self):
        """
        Stops the Create if it is moving.
        """
        wallaby.create_stop()

    # - Constants

    max_speed: float = 500.0
    """
    The fastest Create speed in mm/sec.

    If this value is inaccurate for your robot, you can change it. Do so as
    early in your program as possible (eg. before you create/initialize any
    components.)
    """
