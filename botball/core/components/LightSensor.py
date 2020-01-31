import os
from ... import wallaby
from . import AnalogSensor


class LightSensor(AnalogSensor):
    """
    Represents a light sensor connected to the robot.
    """

    def wait_for_light(self):
        """
        Blocks until light shines on this sensor. Useful for ensuring that your
        robot does not start moving before the signal lights turn on at the
        competition.
        """
        wallaby.wait_for_light(self.port)

    def wait_for_light_if_competition(self):
        """
        Calls `wait_for_light` only if no debug flag has been set.
        """
        if os.getenv("BOTBALL_USE_DEBUG") != "true":
            self.wait_for_light()
