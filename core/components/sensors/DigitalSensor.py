import libwallaby
from ..Component import Component


class DigitalSensor(Component):
    """
    Represents a digital sensor connected to the robot.
    """

    def value(self) -> bool: 
        """ 
        The current readout of the sensor. 
        """ 
        return self._readout() == 1

    # - Readout

    def _readout(self) -> int:
        """
        This function should always return 1 or 0. 
        """ 
        return libwallaby.digital(self.port)
