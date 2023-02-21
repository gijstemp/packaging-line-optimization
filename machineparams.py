from scipy import stats
from state import State
import random
from machineconfig import *


# MACHINE PARAMETERS
# id: the identification of the state,
# transitions: the probability of arriving in each state,
# speed: the distribution function to get the speed of the machine,
# duration: the distribution function to get the duration in current state
###################################################################################
# Depalletizer
# State 0
depal_state_0 = State(
    0,
    {128: 0.886, 1024: 0.108, 2048: 0.006},
    randomGenerator(lambda: [0]),
    randomGenerator(stats.expon.rvs, **{"loc": 1, "scale": 6.829, "size": 1}),
)
# State 128
depal_speed_prob128 = {
    0.0: 0.02,
    300.0: 0.01,
    450.0: 0.04,
    600.0: 0.1,
    750.0: 0.33,
    900.0: 0.27,
    1050.0: 0.2,
    1200.0: 0.04,
}
depal_state_128 = State(
    128,
    {1024: 0.377, 2048: 0.131, 0: 0.492},
    randomGenerator(
        random.choices,
        **{
            "population": list(depal_speed_prob128.keys()),
            "weights": depal_speed_prob128.values(),
            "k": 1,
        }
    ),
    randomGenerator(
        stats.lognorm.rvs, **{"s": 1.595, "loc": -0.0427, "scale": 21.008, "size": 1}
    ),
)
# State 1024
depal_speed_prob1024 = {
    0.0: 0.81,
    150.0: 0.02,
    300.0: 0.02,
    450.0: 0.02,
    600.0: 0.02,
    750.0: 0.04,
    900.0: 0.04,
    1050.0: 0.03,
}
depal_state_1024 = State(
    1024,
    {128: 0.693, 0: 0.306, 2048: 0.001},
    randomGenerator(
        random.choices,
        **{
            "population": list(depal_speed_prob1024.keys()),
            "weights": depal_speed_prob1024.values(),
            "k": 1,
        }
    ),
    randomGenerator(stats.expon.rvs, **{"loc": 1, "scale": 7.418, "size": 1}),
)
# State 2048
depal_speed_prob2048 = {
    0.0: 0.33,
    150.0: 0.09,
    300.0: 0.09,
    450.0: 0.08,
    600.0: 0.05,
    750.0: 0.16,
    900.0: 0.09,
    1050.0: 0.1,
    1200.0: 0.01,
}
depal_dur_prob2048 = {
    1: 128.0,
    6: 6.0,
    3: 7.0,
    9: 3.0,
    15: 1.0,
    10: 1.0,
    4: 5.0,
    2: 8.0,
    8: 2.0,
    5: 5.0,
    7: 3.0,
    11: 3.0,
    21: 1.0,
    13: 1.0,
    83: 1.0,
}
depal_state_2048 = State(
    2048,
    {128: 0.897, 0: 0.092, 1024: 0.011},
    randomGenerator(
        random.choices,
        **{
            "population": list(depal_speed_prob2048.keys()),
            "weights": depal_speed_prob2048.values(),
            "k": 1,
        }
    ),
    randomGenerator(
        random.choices,
        **{
            "population": list(depal_dur_prob2048.keys()),
            "weights": depal_dur_prob2048.values(),
            "k": 1,
        }
    ),
)
# Configuration
Depalletizer = MachineConfig(
    "Depalletizer",
    states=[depal_state_0, depal_state_128, depal_state_1024, depal_state_2048],
)

###################################################################################
# Filler
# State 0
filler_state_0 = State(
    0,
    {128: 0.371, 1024: 0.263, 32768: 0.193, 16384: 0.172},
    randomGenerator(lambda: [0]),
    randomGenerator(stats.expon.rvs, **{"loc": 1.0, "scale": 8.075, "size": 1}),
)
# State 128
filler_speed_prob128 = {841.0: 0.11, 916.0: 0.01, 999.0: 0.01, 1200.0: 0.87}
filler_state_128 = State(
    128,
    {1024: 0.798, 16384: 0.104, 0: 0.080, 32768: 0.018},
    randomGenerator(
        random.choices,
        **{
            "population": list(filler_speed_prob128.keys()),
            "weights": filler_speed_prob128.values(),
            "k": 1,
        }
    ),
    randomGenerator(
        stats.lognorm.rvs, **{"s": 1.208, "loc": -0.078, "scale": 10.795, "size": 1}
    ),
)
# State 1024
filler_speed_prob1024 = {0.0: 0.74, 208.0: 0.2, 721.0: 0.02, 841.0: 0.02, 1200.0: 0.03}
filler_state_1024 = State(
    1024,
    {128: 0.853, 0: 0.063, 16384: 0.048, 32768: 0.063},
    randomGenerator(
        random.choices,
        **{
            "population": list(filler_speed_prob1024.keys()),
            "weights": filler_speed_prob1024.values(),
            "k": 1,
        }
    ),
    randomGenerator(stats.expon.rvs, **{"loc": 1, "scale": 3.106, "size": 1}),
)
# State 16384
filler_speed_prob16384 = {208.0: 0.98, 1200.0: 0.02}
filler_state_16384 = State(
    16384,
    {128: 0.549, 0: 0.27, 1024: 0.172, 32768: 0.009},
    randomGenerator(
        random.choices,
        **{
            "population": list(filler_speed_prob16384.keys()),
            "weights": filler_speed_prob16384.values(),
            "k": 1,
        }
    ),
    randomGenerator(stats.expon.rvs, **{"loc": 1, "scale": 5.558, "size": 1}),
)
# State 32768
filler_speed_prob32768 = {208.0: 0.89, 333.0: 0.11}
filler_state_32768 = State(
    32768,
    {0: 0.364, 128: 0.364, 1024: 0.15, 16384: 0.122},
    randomGenerator(
        random.choices,
        **{
            "population": list(filler_speed_prob32768.keys()),
            "weights": filler_speed_prob32768.values(),
            "k": 1,
        }
    ),
    randomGenerator(stats.pareto.rvs, **{"b": 1, "loc": 0, "scale": 1, "size": 1}),
)
# Configuration
Filler = MachineConfig(
    "Filler",
    states=[
        filler_state_0,
        filler_state_128,
        filler_state_1024,
        filler_state_16384,
        filler_state_32768,
    ],
)

###################################################################################
# Pasteurizer
# State 0
past_dur_prob0 = {
    1: 0.143,
    4: 0.071,
    37: 0.071,
    41: 0.071,
    47: 0.071,
    73: 0.071,
    117: 0.071,
    119: 0.071,
    140: 0.071,
    156: 0.071,
    170: 0.071,
    259: 0.071,
    294: 0.071,
}
past_state_0 = State(
    0,
    {1024: 0.56, 128: 0.44},
    randomGenerator(lambda: [0]),
    randomGenerator(
        random.choices,
        **{
            "population": list(past_dur_prob0.keys()),
            "weights": past_dur_prob0.values(),
            "k": 1,
        }
    ),
)
# State 128
past_dur_prob128 = {
    0: 1.0,
    137: 1.0,
    3: 11.0,
    1: 18.0,
    5: 4.0,
    2: 8.0,
    8: 1.0,
    31: 1.0,
    155: 1.0,
    233: 2.0,
    72: 2.0,
    302: 1.0,
    66: 1.0,
    416: 1.0,
    148: 1.0,
    200: 1.0,
    237: 1.0,
    238: 1.0,
    354: 1.0,
    383: 2.0,
    422: 1.0,
    192: 1.0,
    48: 1.0,
    78: 1.0,
    136: 1.0,
    15: 1.0,
    111: 1.0,
    21: 1.0,
    427: 1.0,
    92: 1.0,
    10: 2.0,
    258: 1.0,
    335: 1.0,
    195: 1.0,
    260: 1.0,
    84: 1.0,
    12: 1.0,
    36: 1.0,
    292: 1.0,
    184: 1.0,
    198: 1.0,
    301: 1.0,
    432: 2.0,
    26: 1.0,
    9: 1.0,
    149: 1.0,
    169: 1.0,
    396: 1.0,
    408: 1.0,
    230: 1.0,
    53: 1.0,
    472: 1.0,
    467: 1.0,
    196: 1.0,
    177: 1.0,
    295: 1.0,
    244: 1.0,
    6: 2.0,
    62: 1.0,
    220: 1.0,
    251: 1.0,
    150: 2.0,
    50: 1.0,
    346: 1.0,
    466: 1.0,
    449: 1.0,
    229: 1.0,
    37: 1.0,
    114: 1.0,
    178: 1.0,
    186: 1.0,
    147: 1.0,
    209: 1.0,
    59: 2.0,
    429: 1.0,
    35: 1.0,
    4: 2.0,
    7: 1.0,
    282: 1.0,
    372: 1.0,
    190: 1.0,
    306: 1.0,
    158: 1.0,
    141: 1.0,
    363: 1.0,
    98: 1.0,
    250: 1.0,
    373: 1.0,
    475: 1.0,
    166: 1.0,
    240: 1.0,
    14: 1.0,
    326: 1.0,
    144: 1.0,
    417: 1.0,
    23: 1.0,
    67: 1.0,
    73: 1.0,
    234: 1.0,
    356: 1.0,
    457: 1.0,
    345: 1.0,
}
past_speed_prob128 = {630: 0.3, 833: 0.088, 1291: 0.612}
past_state_128 = State(
    128,
    {1024: 0.923, 0: 0.077},
    randomGenerator(
        random.choices,
        **{
            "population": list(past_speed_prob128.keys()),
            "weights": past_speed_prob128.values(),
            "k": 1,
        }
    ),
    randomGenerator(
        random.choices,
        **{
            "population": list(past_dur_prob128.keys()),
            "weights": past_dur_prob128.values(),
            "k": 1,
        }
    ),
)
# State 1024
past_speed_prob1024 = {630: 0.286, 833: 0.015, 1291: 0.699}
past_state_1024 = State(
    1024,
    {128: 0.954, 0: 0.046},
    randomGenerator(
        random.choices,
        **{
            "population": list(past_speed_prob1024.keys()),
            "weights": past_speed_prob1024.values(),
            "k": 1,
        }
    ),
    randomGenerator(stats.pareto.rvs, **{"b": 1, "loc": 0, "scale": 1, "size": 1}),
)
# Configuration
Pasteurizer = MachineConfig(
    "Pasteurizer", states=[past_state_0, past_state_128, past_state_1024]
)

###################################################################################
# Labeler 1
# State 0
labeler1_state_0 = State(
    0,
    {128: 0.794, 4: 0.206},
    randomGenerator(lambda: [0]),
    randomGenerator(
        stats.lognorm.rvs, **{"s": 1.209, "loc": -0.012, "scale": 2.678, "size": 1}
    ),
)
# State 4
labeler1_speed_prob4 = {0.0: 0.28, 180.0: 0.09, 181.0: 0.3, 182.0: 0.28, 183.0: 0.05}
labeler1_state_4 = State(
    4,
    {128: 0.798, 0: 0.202},
    randomGenerator(
        random.choices,
        **{
            "population": list(labeler1_speed_prob4.keys()),
            "weights": labeler1_speed_prob4.values(),
            "k": 1,
        }
    ),
    randomGenerator(stats.expon.rvs, **{"loc": 1, "scale": 1.887, "size": 1}),
)
# State 128
labeler1_speed_prob128 = {
    332.0: 0.01,
    333.0: 0.07,
    334.0: 0.09,
    335.0: 0.05,
    336.0: 0.02,
    584.0: 0.02,
    585.0: 0.07,
    586.0: 0.12,
    587.0: 0.1,
    588.0: 0.07,
    589.0: 0.04,
    590.0: 0.02,
    663.0: 0.01,
    664.0: 0.04,
    665.0: 0.06,
    666.0: 0.07,
    667.0: 0.05,
    668.0: 0.03,
    669.0: 0.03,
    670.0: 0.02,
}
labeler1_state_128 = State(
    128,
    {4: 0.503, 0: 0.497},
    randomGenerator(
        random.choices,
        **{
            "population": list(labeler1_speed_prob128.keys()),
            "weights": labeler1_speed_prob128.values(),
            "k": 1,
        }
    ),
    randomGenerator(
        stats.beta.rvs,
        **{"a": 0.645, "b": 57.206, "loc": 1, "scale": 4601.68, "size": 1}
    ),
)
# Configuration
Labeler1 = MachineConfig(
    "Labeler1", states=[labeler1_state_0, labeler1_state_4, labeler1_state_128]
)

###################################################################################
# Labeler 2
# State 0
labeler2_state_0 = State(
    0,
    {128: 0.794, 4: 0.206},
    randomGenerator(lambda: [0]),
    randomGenerator(stats.expon.rvs, **{"loc": 1, "scale": 7.03, "size": 1}),
)
# State 4
labeler2_speed_prob4 = {0.0: 0.27, 215.0: 0.13, 216.0: 0.41, 217.0: 0.16, 218.0: 0.02}
labeler2_state_4 = State(
    4,
    {128: 0.673, 0: 0.327},
    randomGenerator(
        random.choices,
        **{
            "population": list(labeler2_speed_prob4.keys()),
            "weights": labeler2_speed_prob4.values(),
            "k": 1,
        }
    ),
    randomGenerator(stats.expon.rvs, **{"loc": 1, "scale": 1.055, "size": 1}),
)
# State 128
labeler2_speed_prob128 = {
    343.0: 0.04,
    344.0: 0.12,
    345.0: 0.08,
    346.0: 0.03,
    578.0: 0.02,
    579.0: 0.08,
    580.0: 0.14,
    581.0: 0.1,
    582.0: 0.06,
    583.0: 0.04,
    584.0: 0.04,
    585.0: 0.01,
    663.0: 0.03,
    664.0: 0.08,
    665.0: 0.05,
    666.0: 0.03,
    667.0: 0.03,
    668.0: 0.02,
}
labeler2_state_128 = State(
    128,
    {4: 0.603, 0: 0.397},
    randomGenerator(
        random.choices,
        **{
            "population": list(labeler2_speed_prob128.keys()),
            "weights": labeler2_speed_prob128.values(),
            "k": 1,
        }
    ),
    randomGenerator(
        stats.beta.rvs,
        **{"a": 0.790, "b": 150.314, "loc": -3.840e-25, "scale": 47684.3, "size": 1}
    ),
)
# Configuration
Labeler2 = MachineConfig(
    "Labeler2", states=[labeler2_state_0, labeler2_state_4, labeler2_state_128]
)

###################################################################################
# Capper
# State 0
gpi_state_0 = State(
    0,
    {128: 1},
    randomGenerator(lambda: [0]),
    randomGenerator(stats.expon.rvs, **{"loc": 1.0, "scale": 4.078, "size": 1}),
)
# State 128
gpi_speed_prob128 = {
    0.0: 0.01,
    420.0: 0.13,
    600.0: 0.18,
    840.0: 0.46,
    1080.0: 0.02,
    1200.0: 0.11,
    1260.0: 0.01,
    1320.0: 0.02,
    1440.0: 0.07,
}
gpi_state_128 = State(
    128,
    {0: 1},
    randomGenerator(
        random.choices,
        **{
            "population": list(gpi_speed_prob128.keys()),
            "weights": gpi_speed_prob128.values(),
            "k": 1,
        }
    ),
    randomGenerator(
        stats.lognorm.rvs, **{"s": 1.406, "loc": -0.0136, "scale": 8.660, "size": 1}
    ),
)
# Configuration
Capper = MachineConfig("Capper", states=[gpi_state_0, gpi_state_128])

###################################################################################
# Packer
# State 0
sn64_state_0 = State(
    0,
    {128: 1},
    randomGenerator(lambda: [0]),
    randomGenerator(stats.expon.rvs, **{"loc": 1.0, "scale": 5.864, "size": 1}),
)
# State 128
sn64_speed_prob128 = {
    0.0: 0.03,
    390.0: 0.08,
    480.0: 0.03,
    510.0: 0.04,
    540.0: 0.18,
    550.0: 0.01,
    570.0: 0.01,
    600.0: 0.04,
    630.0: 0.02,
    660.0: 0.1,
    690.0: 0.03,
    720.0: 0.23,
    750.0: 0.02,
    780.0: 0.07,
    900.0: 0.07,
    1000.0: 0.01,
    1050.0: 0.02,
}
sn64_state_128 = State(
    128,
    {0: 1},
    randomGenerator(
        random.choices,
        **{
            "population": list(sn64_speed_prob128.keys()),
            "weights": sn64_speed_prob128.values(),
            "k": 1,
        }
    ),
    randomGenerator(
        stats.lognorm.rvs, **{"s": 1.59, "loc": -0.0136, "scale": 10.040, "size": 1}
    ),
)
# Configuration
Packer = MachineConfig("Packer", states=[sn64_state_0, sn64_state_128])

###################################################################################
# Palletizer 1
# State 0
pal1_state_0 = State(
    0,
    {128: 1},
    randomGenerator(lambda: [0]),
    randomGenerator(stats.expon.rvs, **{"loc": 1, "scale": 9.135, "size": 1}),
)
# State 128
pal1_speed_prob128 = {0.0: 0.57, 1200: 0.43}
pal1_state_128 = State(
    128,
    {0: 1},
    randomGenerator(
        random.choices,
        **{
            "population": list(pal1_speed_prob128.keys()),
            "weights": pal1_speed_prob128.values(),
            "k": 1,
        }
    ),
    randomGenerator(
        stats.beta.rvs,
        **{"a": 0.614, "b": 365.763, "loc": -4.511e-28, "scale": 16265.5, "size": 1}
    ),
)
# Configuration
Palletizer1 = MachineConfig("Palletizer_1", states=[pal1_state_0, pal1_state_128])

###################################################################################
# Palletizer 2
# State 0
pal2_state_0 = State(
    0,
    {128: 1},
    randomGenerator(lambda: [0]),
    randomGenerator(
        stats.t.rvs, **{"df": 0.806, "loc": 3.339, "scale": 2.5, "size": 1}
    ),
)
# State 128
pal2_speed_prob128 = {0.0: 0.63, 1200: 0.37}
pal2_state_128 = State(
    128,
    {0: 1},
    randomGenerator(
        random.choices,
        **{
            "population": list(pal2_speed_prob128.keys()),
            "weights": pal2_speed_prob128.values(),
            "k": 1,
        }
    ),
    randomGenerator(
        stats.t.rvs, **{"df": 0.579, "loc": 8.931, "scale": 13.984, "size": 1}
    ),
)
# Configuration
Palletizer2 = MachineConfig("Palletizer_2", states=[pal2_state_0, pal2_state_128])
