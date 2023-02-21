import numpy as np
from dataclasses import dataclass
import simpy
from typing import Tuple
from buffer import Buffer
from state import State
from machineconfig import MachineConfig

# Class setup for a Machine
@dataclass
class Machine(object):
    """
    A machine produces units at a fixed processing speed,
    takes units from a store before and puts units into a store after.
    """

    def __init__(
        self,
        env: simpy.Environment,
        name: str,
        machine_config: MachineConfig,
        initial_state: int,
        in_q: Buffer,
        out_q: Buffer,
        event_list: list,
    ):
        self.env = env
        self.name = name
        self.machine_config = machine_config
        self.state: State = machine_config.state(initial_state)
        self.in_q = in_q
        self.out_q = out_q
        self.count = 0
        self.produced = None
        self.idle_parts = 0
        self.tailback = 0
        self.lack = 0
        self.event_list = event_list
        # Start the producing process
        self.process = env.process(self.produce())

    def produce(self):
        """
        Produce parts as long as the simulation runs.
        It is prone to breaking down and being repaired.
        """
        last_state_switch = self.env.now
        time_in_state = self.state.new_duration()
        # print(f"init {self.name} in state {self.state.id} for {time_in_state} minutes")
        while True:
            pspeed = self.get_speed()
            # Update count and what goes out and in buffers
            start_producing = self.in_q.get_parts(pspeed)
            # Check whether there is a lack
            if start_producing < pspeed and pspeed != 0:
                self.lack = 1
            else:
                self.lack = 0
            success_produced = self.out_q.put_parts(start_producing)
            # Check whether there is a tailback and set pspeed to 0
            if success_produced < pspeed and self.lack == 0:
                pspeed = 0
                self.tailback = 1
                self.idle_parts += start_producing - success_produced
            else:
                self.tailback = 0
            self.produced = success_produced
            self.count += self.produced
            # While machine has not been in state for given time
            if self.env.now == last_state_switch + time_in_state:
                self.state, time_in_state = self.get_next_state()
                last_state_switch = self.env.now
            self.event_list.append(
                {
                    "Time": self.env.now,
                    "Machine": self.name,
                    "State": self.state.id,
                    "Set speed": pspeed,
                    "Actual speed": self.produced,
                    "Count": self.count,
                    "Tailback": self.tailback,
                    "Lack": self.lack,
                    "Simulation": None,
                }
            )
            yield self.env.timeout(1)

    def get_speed(self):
        speed = 0
        if not (self.tailback or self.lack):
            speed = self.state.new_speed()
        return speed

    def get_next_state(self) -> Tuple[int, int]:
        # Select a state at random with given probabilities
        next_state_id = self.state.next_state_id()
        next_state = self.machine_config.state(next_state_id)
        # Find time in state (Complete and fill in correct params)
        time_in_state = next_state.new_duration()
        return next_state, time_in_state
