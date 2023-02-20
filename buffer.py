import numpy as np
from dataclasses import dataclass

# Setup for buffer
@dataclass
class Buffer(object):
    """
    This is the class that defines the buffers of the packaging line.
    The function of this class is to get parts from a machine before
    it and to put parts into the machine after it.
    """

    def __init__(self, id: int, max_capacity: int = np.inf, current_parts: int = 0):

        self.id = id
        self.max_capacity = max_capacity
        self.current_parts = current_parts

    def get_parts(self, amount: int):
        """
        This function make the buffer release parts to the machine after it.
        It takes the minimum between the amount (which is called from the machine after it)
        and the current amount of parts in the buffer, and "gives" these to the machine after it.

        If the buffer is empty it says so.
        """
        result_out = min([amount, self.current_parts])
        self.current_parts -= result_out
        return result_out

    def put_parts(self, amount: int) -> int:
        """
        This function make the buffer receive parts to the machine after it.
        It takes the minimum between the amount (which is called from the machine before it)
        and the current space in the buffer, and "takes" these from the machine before it.

        If the buffer is full it says so.
        """
        buffer_space = self.max_capacity - self.current_parts
        result_in = min([amount, buffer_space])
        self.current_parts += result_in
        return result_in
