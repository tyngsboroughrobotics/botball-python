try:
    from typing import Callable
except ImportError:
    pass

import os
from ..procedure import Procedure


def choose_game_procedure(demobot: Procedure, create: Procedure, **run_args) -> Callable[[], None]:
    """
    Given two game procedures for a Demobot robot and a iRobot Create robot,
    returns a function that can be called to execute the appropriate procedure
    with the appropriate settings given the configuration files.

    - `demobot`: The procedure to execute when running this program on a Demobot
    robot.

    - `create`: The procedure to execute when running this program on an iRobot
    Create robot.

    - `run_args`: Any additional arguments to pass to the `run` function of the
    chosen procedure.

    ## Configuration files

    The following files will affect the function that is returned:

    - `/etc/ths-botball-conf/demobot`: If this exists, this function returns the
    `run` function of the `demobot` parameter.

    - `/etc/ths-botball-conf/create`: If this exists, this function returns the
    `run` function of the `create` parameter.

        - If both of these are set, `demobot` has precedence.

        - If neither of these are set, this function raises a
        `FileNotFoundError`.

    - `/etc/ths-botball-conf/demobot`: If this exists in addition to one of the
    above, this function returns the appropriate `run` function with its `debug`
    parameter set to `True`.
    """

    config_path = "/etc/ths-botball-conf"

    if os.path.exists(f"{config_path}/demobot"):
        procedure_to_use = demobot
    elif os.path.exists(f"{config_path}/demobot"):
        procedure_to_use = create
    else:
        raise ValueError("Neither BOTBALL_USE_DEMOBOT nor BOTBALL_USE_CREATE found in environment variables")

    debug = os.path.exists(f"{config_path}/debug")

    return lambda: procedure_to_use.run(debug=debug, **run_args)
