# Packaging Line Optimization
## Overview
This project simulates and optimizes a soft drink production line with eight machines: 
- depalletizer, 
- filler, 
- pasteurizer, 
- labeler 1, 
- labeler 2, 
- capper, 
- packer, and 
- palletizer 1 and 2. 

The simulation runs for a specified time and tracks the machines' states, speeds, and the products produced. 
The optimization model uses this data to allocate the machines' speeds to maximize production while respecting the buffers' capacities.

This is the result of my MSc. master thesis and the research paper can be found at https://thesis.eur.nl/pub/63449

## Installation and requirements
To run the simulation and the optimization model, you will need Python 3 and the following packages:

- numpy
- pandas
- simpy
- Gurobi

You can install these packages with pip:
```
pip install numpy pandas simpy gurobipy
```
To use Gurobi, you will also need to have a valid license.

## Usage
The simulation and optimization are divided into several files:

- `machineparams.py`: contains the parameters for each machine.
- `buffer.py`: contains the class definition for the Buffer objects.
- `machine.py`: contains the class definition for the Machine objects.
- `state.py`: contains the class definition for the State objects.
- `simulation.py`: contains the code to run the simulation and generate the log.
- `1. create_linprog_df.ipynb`: a Jupyter notebook that creates a new CSV file from the log to be used in the linear programming.
- `2. LP_model.ipynb`: a Jupyter notebook that contains the complete code for the linear programming optimization model using licensed Gurobi.

To run the simulation and generate the log, you can simply run simulation.py:
```
python simulation.py
```
This will run the simulation for 480 time units, generate a log of the events, and save it to data/sim_log.csv. To change the number of simulations that are run change the variable `num_sim`.

To run the optimization model, you need to have a valid Gurobi license. First run `1. create_linprog_df.ipynb` in a Jupyter notebook environment to create the correct .csv file and save it in data/linprog_df.csv. 
Thereafter run `2. LP_model.ipynb` in a Jupyter notebook environment. This will load the log from data/sim_log.csv, create a linear programming model to optimize the machine speeds, and generate a new CSV file with the results in data/df_optvalues.csv.

## Contributing
If you want to contribute to this project, feel free to open an issue or submit a pull request on GitHub.

## Credits
This project was created by Gijs Tempelman for his MSc. Business Administration and Management Thesis at Erasmus University Rotterdam .
