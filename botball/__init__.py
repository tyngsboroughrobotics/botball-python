from . import core, libwallaby

# Add README to documentation
with open("README.md") as readme:
    global __doc__
    __doc__ = "".join(readme.readlines())
