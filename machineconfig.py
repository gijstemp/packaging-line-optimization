from dataclasses import dataclass
from typing import List, Dict, Callable, Union, Any, Tuple
from state import State


class MachineConfigError(Exception):
    """
    Custom exception for configuration errors in machines.
    """

    pass


@dataclass
class MachineConfig:
    """
    This class configures a machine to run at a certain speed, given the current state and duration.
    """

    name: str
    states: List[State]

    def state(self, state_id: int) -> State:
        """
        Returns the state with the specified ID from the list of states.

        Args:
            state_id (int): ID of the state to return.

        Raises:
            MachineConfigError: If the specified state ID is not found in the list of states.
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
        Returns the ID of the next state that the machine will transition to from the current state.

        Args:
            current_state (int): ID of the current state.
        """
        return self.state(current_state).next_state_id()

    def new_speed(self, current_state: int) -> float:
        """
        Returns a new speed for producing the units based on the distribution of possible speeds in the current state.

        Args:
            current_state (int): ID of the current state.
        """
        return self.state(current_state).new_speed()

    def new_duration(self, current_state: int) -> int:
        """
        Returns a new duration for the machine to be in the current state based on the distribution of possible durations.

        Args:
            current_state (int): ID of the current state.
        """
        return max([1, self.state(current_state).new_duration()])


@dataclass
class randomGenerator:
    """
    This class generates a random value using a specified function and arguments.
    """

    function: Callable
    kwargs: Dict[str, Any]

    def new(self) -> Union[float, int]:
        """
        Returns a new random value based on the specified function and arguments.
        """
        return self.function(**self.kwargs)[0]
