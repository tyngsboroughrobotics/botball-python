from botball import wallaby
from .Motor import Motor
from ..Direction import Direction


class WheelGroup(object):
    """
    Use a wheel group to make it easier to control two motors representing a
    left and right wheel simultaneously.
    """

    left_motor: Motor
    """
    The left motor.
    """

    right_motor: Motor
    """
    The right motor.
    """

    def __init__(self, left: Motor, right: Motor):
        self.left_motor = left
        self.right_motor = right

    # - Driving

    def drive_with(
        self,
        left_direction: Direction = Direction.Forward, left_distance: float = 100,
        right_direction: Direction = Direction.Forward, right_distance: float = 100,
        block: bool = True, sleep: bool = True
    ):
        """
        Drive with different parameters for both wheels.

        See `Motor.move()` for information on the other parameters.
        """
        left_motor = self.left_motor.__copy__()
        right_motor = self.right_motor.__copy__()

        left_motor.move(left_direction, mm=left_distance, block=False, sleep=False)
        right_motor.move(right_direction, mm=right_distance, block=block, sleep=False)

        if block:
            wallaby.off(left_motor.port)

        if sleep:
            wallaby.msleep(Motor.default_sleep_time)

    def drive(
        self,
        direction: Direction = Direction.Forward,
        mm: float = 100,
        block: bool = True, sleep: bool = True
    ):
        """
        Drive with the same parameters for both wheels.

        See `Motor.move()` for information on the other parameters.
        """

        self.drive_with(
            left_direction=direction,
            right_direction=direction,
            left_distance=mm,
            right_distance=mm,
            block=block,
            sleep=sleep
        )

    # - Turning

    def turn_right(self, degrees: float, block: bool = True, sleep: bool = True):
        """
        Turn right in place. Offsets are ignored when using this function.

        - `degrees`: The number of degrees to turn right. 180 indicates a half
        turn, and 360 degrees indicates a full turn (eg. back where it
        started.)

        See `Motor.move()` for information on the other parameters.
        """

        distance = self.turn_amount(degrees) * degrees

        self.drive_with(
            left_direction=Direction.Forward,
            right_direction=Direction.Backward,
            left_distance=distance,
            right_distance=distance,
            block=block,
            sleep=sleep
        )

    def turn_left(self, degrees: float, block: bool = True, sleep: bool = True):
        """
        Turn left in place. Offsets are ignored when using this function.

        - `degrees`: The number of degrees to turn right. 180 indicates a half
        turn, and 360 degrees indicates a full turn (eg. back where it
        started.)

        See `Motor.move()` for information on the other parameters.
        """

        distance = self.turn_amount(degrees) * degrees

        self.drive_with(
            left_direction=Direction.Backward,
            right_direction=Direction.Forward,
            left_distance=distance,
            right_distance=distance,
            block=block,
            sleep=sleep
        )

    # - Configuration

    @staticmethod
    def turn_amount(degrees) -> float:
        """
        The distance (in mm) forward the left wheel and backward the right wheel
        should travel when a wheel group is performing a clockwise turn, and
        vice versa.

        This function has been generated using regression for the following turn
        amounts:

        - 45 degrees = 1.175
        - 90 degrees = 1.2425
        - 180 degrees = 1.35
        - 360 degrees = 1.425
        """
        return -2.781096509 * (10 ** -6) * (degrees ** 2) + 1.922759857 * (10 ** -3) * degrees + 1.093333333

