import os
from ..procedure import *


def choose_game_procedure(demobot: Procedure, create: Procedure, **run_args) -> Callable[[], None]:
    """
    Given two game procedures for a Demobot robot and a iRobot Create robot,
    returns a function that can be called to execute the appropriate procedure
    with the appropriate settings given the environment variables.

    - `demobot`: The procedure to execute when running this program on a Demobot
    robot.

    - `create`: The procedure to execute when running this program on an iRobot
    Create robot.

    - `run_args`: Any additional arguments to pass to the `run` function of the
    chosen procedure.

    ## Environment variables

    The following environment variables will affect the function that is
    returned:

    - `BOTBALL_USE_DEMOBOT`: If set, returns the `run` function of the `demobot`
    parameter.

    - `BOTBALL_USE_CREATE`: If set, returns the `run` function of the `create`
    parameter.

        - If both of these are set, `BOTBALL_USE_DEMOBOT` has precedence.
        - If neither of these are set, this function raises a `ValueError`.

    - `BOTBALL_USE_DEBUG`: If set in addition to one of the above, returns the
    appropriate `run` function with its `debug` parameter set to `True`.
    """

    if "BOTBALL_USE_DEMOBOT" in os.environ:
        procedure_to_use = demobot
    elif "BOTBALL_USE_CREATE" in os.environ:
        procedure_to_use = create
    else:
        raise ValueError("Neither BOTBALL_USE_DEMOBOT nor BOTBALL_USE_CREATE found in environment variables")

    debug = "BOTBALL_USE_DEBUG" in os.environ

    return lambda: procedure_to_use.run(debug=debug, **run_args)
