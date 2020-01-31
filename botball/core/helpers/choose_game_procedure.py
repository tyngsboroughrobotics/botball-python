from typing import Callable, Dict
import os
from ..procedure import Procedure


class RobotConfig(object):
    """
    Represents the configuration of the target robot controller.
    """

    robot_type: str
    """
    The type of robot targeted.
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

        - `/etc/ths-botball-conf/robot_type`: If this exists, `robot_type` is set
        to `"demobot"`.

        - `/etc/ths-botball-conf/debug_enabled`: If this exists, `debug_enabled`
        is set to `True`.
        """

        with open(f"{self.config_path}/robot_type") as robot_type_file:
            self.robot_type = robot_type_file.read()

        self.debug_enabled = os.path.exists(f"{self.config_path}/debug_enabled")

    config_path = "/etc/ths-botball-conf"
    """
    The path to the configuration files on the robot. You shouldn't need to
    change this if you use the default project setup.
    """


def choose_game_procedure(procedure_map: Dict[str, Procedure], **run_args) -> Callable[[], None]:
    """
    Returns a function that can be called to execute the appropriate procedure
    with the appropriate settings given the current robot configuration.

    - `procedure_map`: The map of robot names to procedures.

    - `run_args`: Any additional arguments to pass to the `run` function of the
    chosen procedure.
    """

    config = RobotConfig()
    procedure_to_use = procedure_map[config.robot_type]

    return lambda: procedure_to_use.run(debug=config.debug_enabled, **run_args)
