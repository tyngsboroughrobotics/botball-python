try:
    from ctypes import cdll
    bindings = cdll.LoadLibrary("/usr/lib/libwallaby.so")
except:
    print("WARNING: Could not load libwallaby.so. This is OK if you're \
generating documentation but is bad if you're running on the robot.")
    from . import bindings_stubs as bindings

from .components import *
from .create import *
from .helpers import *
from .procedure import *

try:
    # Add README to documentation
    with open("README.md") as readme:
        global __doc__
        __doc__ = "".join(readme.readlines())
except FileNotFoundError:
    pass
