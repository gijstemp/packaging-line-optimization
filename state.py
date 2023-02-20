import random
from dataclasses import dataclass
from typing import List, Dict, Callable, Union, Any, Tuple


@dataclass
class State:
    """
    Every machine has a few different states that it can operate in. Basically it is dictates
    the speeds that the machine produces the products with and for how long.

    This class calls variables as given in the respective machine parameters.
    """

    id: int
    transitions: Dict[int, float]
    speed: Callable
    duration: Callable

    def __post_init__(self) -> None:
        self.state_population = list(self.transitions.keys())
        self.weights = self.transitions.values()

    def next_state_id(self) -> int:
        """
        Calls the next state the machine will be in
        """
        return random.choices(self.state_population, self.weights, k=1)[0]

    def new_speed(self) -> Union[float, int]:
        """
        Calls the new speed that the machine will produce units with
        """
        return self.speed.new()

    def new_duration(self) -> int:
        """
        Calls the duration of the following state.
        """
        return int(self.duration.new())
