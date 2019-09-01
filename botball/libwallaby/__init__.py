try:
    # The actual code is located in _bindings.py, but it will be mapped to
    # bindings.py during the build. This way we can use the type stub in PyCharm
    # and still have access to the raw bindings on the Wallaby.
    from .bindings import *
except ImportError:
    print("ERROR: Using libwallaby on development machine")
    exit(1)
