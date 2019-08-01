import libwallaby
from ..Component import Component


class AnalogSensor(Component): 
    """
    Represents an analog sensor connected to the robot.
    """ 

    @classmethod
    def min_value(cls) -> int:
        """
        The lowest readout this sensor will give.
        """
        return 0

    @classmethod
    def max_value(cls) -> int:
        """
        The highest readout this sensor will give. 
        """ 
        return 4095

    def value(self) -> int:
        """
        The current readout of this sensor. 
        
        This value will always be between `AnalogSensor.min_value()` and
        `AnalogSensor.max_value()`.
        """ 
        return self._readout()

    def percent_value(self) -> float: 
        """ 
        The current sensor readout expressed between 0.0 and 1.0. 
        """ 
        return self.value() / self.max_value()

    # - Readout

    def _readout(self) -> int:
        return libwallaby.analog(self.port)
