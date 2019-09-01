try:
    from typing import Optional, Callable, Union
except ImportError:
    pass


class Step(object): 
    """
    Represents a step in a procedure. Use the `@step()` decorator to create
    steps.
    """

    name: str
    """
    The name of the step. Appears when running in a procedure.
    """

    description: Optional[str] 
    """
    An optional description of the step. Not used by the program, but allows
    others working on the codebase to understand what this step does.
    """

    action: Union[Callable[[bool], None], Callable[[], None]]
    """
    The function that is executed when the step is ran in a procedure. A boolean
    is passed indicating if debug mode is set or not, so your implementation can
    display debug info appropriately.
    """

    def __init__(self, name: str, description: Optional[str], action: Callable[[bool], None]):
        self.name = name 
        self.description = description
        self.action = action 

    def run(self, debug: bool):
        try:
            self.action(debug)
        except TypeError:
            # noinspection PyArgumentList
            self.action()

    def __call__(self, *args, **kwargs):
        self.run(*args, **kwargs)


def step(name: str, description: Optional[str] = None):
    return lambda fn: Step(name=name, description=description, action=fn)
