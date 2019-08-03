try:
    from .bindings import *
except ImportError:
    print("WARNING: Using libwallaby on development machine")

# Add README to documentation
with open("libwallaby/README.md") as readme:
    global __doc__
    __doc__ = "".join(readme.readlines())
