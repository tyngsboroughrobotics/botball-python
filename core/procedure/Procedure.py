import libwallaby
from typing import List
from datetime import datetime
from .Step import Step


class Procedure(object):
    """
    Represents a procedure defined by a series of steps.
    """

    name: str 

    steps: List[Step]
    """
    An ordered list of all steps in the procedure.
    """

    def __init__(self, name: str, steps: List[Step] = None):
        self.name = name 
        self.steps = steps or []

    def add_step(self, step: Step):
        """
        Adds a step to the procedure.
        """
        self.steps.append(step)

    def add_steps(self, steps: List[Step]):
        """
        Adds multiple steps to the procedure.
        """
        self.steps += steps

    # - Running the procedure

    def run(self, in_between_delay: int = 0, debug: bool = False):
        """
        Runs the procedure.

        - `in_between_delay`: The delay to sleep for in between steps.

        - `debug`: Whether to print information about the starting and stopping
        of steps.
        """

        def debug_print(string: str):
            if debug:
                print(string)

        procedure_start = datetime.now()
        debug_print(f"#START# procedure {self.name}")

        for i, step in enumerate(self.steps):
            step_start = datetime.now()
            debug_print(f"#START# step #{i + 1}: {step.name}")

            step.run(debug)
            
            step_end = datetime.now()
            step_elapsed = (step_end - step_start).total_seconds()

            debug_print(f"##END## step #{i + 1}: {step.name} in {step_elapsed} seconds")

            if in_between_delay > 0:
                libwallaby.msleep(in_between_delay)

        procedure_end = datetime.now()
        procedure_elapsed = (procedure_end - procedure_start).total_seconds()

        debug_print(f"##END## procedure {self.name} in {procedure_elapsed} seconds")
