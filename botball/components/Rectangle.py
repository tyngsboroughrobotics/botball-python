class Rectangle(object):
    """
    Represents the bounding box of an object in the field of view.
    """ 

    x: int = 0 
    y: int = 0 
    width: int = 0 
    height: int = 0 

    def __init__(self, c_rect):
        """
        Bridge a C `bbox` instance to a value of this type.
        """

        self.x = c_rect.x 
        self.y = c_rect.y 
        self.width = c_rect.width 
        self.height = c_rect.height
