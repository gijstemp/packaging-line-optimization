from dataclasses import dataclass
from typing import List, Dict, Callable, Union, Any, Tuple
from state import State

# Configuration
class MachineConfigError(Exception):
    pass


@dataclass
class MachineConfig:
    """
    This is what configures the machine to run at a certain speed given
    the current state for a chosen duration.
    """

    name: str
    states: List[State]

    def state(self, state_id: int) -> State:
        """
        Searches for the next state called from the possibilities.
        """
        try:
            return next(
                (state for state in self.states if state.id == state_id),
            )
        except StopIteration:
            raise MachineConfigError(
                f"Config error in machines, since state {state_id} is not found in machine {self.name}"
            )

    def next_state_id(self, current_state: int) -> int:
        """
        Returns the next state called from the possibilities.
        """
        return self.state(current_state).next_state_id()

    def new_speed(self, current_state: int) -> float:
        """
        Returns the new speed for producing the units called from the distribution of possible speeds.
        """
        return self.state(current_state).new_speed()

    def new_duration(self, current_state: int) -> int:
        """
        Returns the new duration that the machine will be in the state called from the distribution of possible speeds.
        """
        return max([1, self.state(current_state).new_duration()])


class randomGenerator:
    """
    This ensures that a random value can be picked when asked for.
    """

    def __init__(self, function, **kwargs) -> None:
        self.function = function
        self.kwargs = kwargs

    def new(self) -> Union[float, int]:
        """
        Using the given functiona and keyword arguments, a random value is returned.
        """
        return self.function(**self.kwargs)[0]
