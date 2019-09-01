def scale(x: float, in_min: float, in_max: float, out_min: float, out_max: float) -> float:
    """
    Scales a number from one range to another.

    >>> scale(5, 1, 10, 1, 100)
    50
    """
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
