from .core import *
from .wallaby import *

try:
    # Add README to documentation
    with open("README.md") as readme:
        global __doc__
        __doc__ = "".join(readme.readlines())
except FileNotFoundError:
    pass
