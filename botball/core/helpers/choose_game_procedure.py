try:
    from typing import Callable
except ImportError:
    pass

import os
from ..procedure import Procedure


class RobotConfig(object):
    """
    Represents the configuration of the target robot controller.
    """

    robot_type: str
    """
    The type of robot targeted. This will either be `"demobot"` or `"create"`.
    """

    debug_enabled: bool
    """
    Whether debugging is enabled on the target robot.
    """

    def __init__(self):
        """
        Create a new instance of `RobotConfig` with the current configuration
        from the filesystem.

        ## Configuration files

        The following files will affect the configuration:

        - `/etc/ths-botball-conf/demobot`: If this exists, `robot_type` is set
        to `"demobot"`.

        - `/etc/ths-botball-conf/create`: If this exists, `robot_type` is set to
        `"create"`.

            - If both of these are set, `demobot` has precedence.

            - If neither of these are set, a `FileNotFoundError` is raised.

        - `/etc/ths-botball-conf/demobot`: If this exists in addition to one of
        the above, `debug_enabled` is set to `True`.
        """

        if os.path.exists(f"{RobotConfig.config_path}/demobot"):
            self.robot_type = "demobot"
        elif os.path.exists(f"{RobotConfig.config_path}/demobot"):
            self.robot_type = "create"
        else:
            raise FileNotFoundError("Robot controller not configured as Demobot or Create")

        self.debug_enabled = os.path.exists(f"{RobotConfig.config_path}/debug")

    config_path = "/etc/ths-botball-conf"
    """
    The path to the configuration files on the robot. You shouldn't need to
    change this if you use the default project setup.
    """


def choose_game_procedure(demobot: Procedure, create: Procedure, **run_args) -> Callable[[], None]:
    """
    Given two game procedures for a Demobot robot and a iRobot Create robot,
    returns a function that can be called to execute the appropriate procedure
    with the appropriate settings given the current robot configuration.

    - `demobot`: The procedure to execute when running this program on a Demobot
    robot.

    - `create`: The procedure to execute when running this program on an iRobot
    Create robot.

    - `run_args`: Any additional arguments to pass to the `run` function of the
    chosen procedure.
    """

    config = RobotConfig()

    if config.type == "demobot":
        procedure_to_use = demobot
    else:
        procedure_to_use = create

    return lambda: procedure_to_use.run(debug=config.debug_enabled, **run_args)
