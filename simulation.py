import numpy as np
import pandas as pd
import simpy
from buffer import Buffer
from machine import Machine
from machineparams import *
from datetime import datetime


# Time for the simulation to run
RUN_TIME = 481


def run_sim(i):
    # The buffers
    buffer_0 = Buffer("Buffer_0", current_parts=np.inf)
    buffer_1 = Buffer("Buffer_1", max_capacity=3256)  #
    buffer_2 = Buffer("Buffer_2", max_capacity=3400)  #
    buffer_3 = Buffer("Buffer_3", max_capacity=3366)  #
    buffer_4 = Buffer("Buffer_4", max_capacity=3420)  #
    buffer_5 = Buffer("Buffer_5", max_capacity=3530)  #
    buffer_6 = Buffer("Buffer_6", max_capacity=35612)  #
    buffer_7 = Buffer("Buffer_7")

    # The machines
    depalletizer = Machine(
        env, "Depalletizer", Depalletizer, 128, buffer_0, buffer_1, event_list
    )
    filler = Machine(env, "Filler", Filler, 128, buffer_1, buffer_2, event_list)
    pasteurizer = Machine(
        env, "Pasteurizer", Pasteurizer, 128, buffer_2, buffer_3, event_list
    )
    labeler_1 = Machine(env, "Labeler_1", Labeler1, 128, buffer_3, buffer_4, event_list)
    labeler_2 = Machine(env, "Labeler_2", Labeler2, 128, buffer_3, buffer_4, event_list)
    capper = Machine(env, "Capper", Capper, 128, buffer_4, buffer_5, event_list)
    packer = Machine(env, "Packer", Packer, 128, buffer_5, buffer_6, event_list)
    palletizer_1 = Machine(
        env, "Palletizer_1", Palletizer1, 128, buffer_6, buffer_7, event_list
    )
    palletizer_2 = Machine(
        env, "Palletizer_2", Palletizer2, 128, buffer_6, buffer_7, event_list
    )

    # Execute
    env.run(until=RUN_TIME)
    return event_list


event_list = []
begin_time = datetime.now()
# Number of simulations
num_sim = 10
for i in range(num_sim):
    print(f"---------- STARTING SIMULATION {i+1} ----------")
    sim_start = datetime.now()  # To see how long each simulation takes
    event_list.append(
        {
            "Time": 0.00,
            "Machine": "All",
            "State": "Simulation start",
            "Set speed": 0,
            "Actual speed": 0,
            "Count": 0,
            "Tailback": 0,
            "Lack": 0,
            "Simulation": int(i + 1),
        }
    )
    # Create environment and start the setup process
    env = simpy.Environment()
    run_sim(i)
    print(datetime.now() - sim_start)

# To see the total time of all simulations
print(f"The total runtime for {num_sim} is {datetime.now() - begin_time}")

log = pd.DataFrame(event_list)
log["Simulation"].ffill(inplace=True)
log.to_csv("data/sim_log.csv")
