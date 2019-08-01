class Component(object):
    """
    Defines a component to be plugged into the robot.
    """

    port: int 
    """ 
    The port on the robot that this component is plugged into.
    """

    def __init__(self, port: int):
        self.port = port
