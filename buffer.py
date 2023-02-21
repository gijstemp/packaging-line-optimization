import numpy as np
from dataclasses import dataclass


@dataclass
class Buffer(object):
    """
    This is the class that defines the buffers of the packaging line.
    The function of this class is to get parts from a machine before it
    and to put parts into the machine after it.
    """

    def __init__(self, id: int, max_capacity: int = np.inf, current_parts: int = 0):
        """
        Initializes a buffer object with the given id, maximum capacity, and current number of parts.

        :param id: The identifier of the buffer.
        :param max_capacity: The maximum number of parts that the buffer can hold.
        :param current_parts: The current number of parts in the buffer (defaults to 0).
        """
        self.id = id
        self.max_capacity = max_capacity
        self.current_parts = current_parts

    def get_parts(self, amount: int) -> int:
        """
        This function makes the buffer release parts to the machine after it.
        It takes the minimum between the amount (which is called from the machine after it)
        and the current amount of parts in the buffer, and returns this value.

        :param amount: The number of parts that the machine after the buffer requests.
        :return: The number of parts released by the buffer to the machine after it.
        """
        result_out = min([amount, self.current_parts])
        self.current_parts -= result_out
        return result_out

    def put_parts(self, amount: int) -> int:
        """
        This function makes the buffer receive parts from the machine before it.
        It takes the minimum between the amount (which is called from the machine before it)
        and the current space in the buffer, and returns this value.

        :param amount: The number of parts that the machine before the buffer sends.
        :return: The number of parts received by the buffer from the machine before it.
        """
        buffer_space = self.max_capacity - self.current_parts
        result_in = min([amount, buffer_space])
        self.current_parts += result_in
        return result_in
