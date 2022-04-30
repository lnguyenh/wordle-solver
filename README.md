# Wordle Solver

## About
I thought it would be fun to make a Wordle solver in Python. This repo is a playground for it.

## Quickstart

### Setup
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

### Run The Fully Automatic Solve 
This uses Selenium to open the Wordle page in a browser and solves the puzzle of the day without any user input.
```
python browser_solver.py
```

### Run The Assistant Solver
This is a CLI tool where you tell the program about new constraints, and it will suggest a few words for the next guess.
```
python cli_assistant_solver.py
```

Example usage:
```
# indexes start at 1
exclude r 1
correct a 1
almost t 5

exclude rio
correct a 1 b 2 c 3
almost x 1 v 2
```

### Run A Complete Simulation
You choose a solution word and a starting word and let the program find the solution. Each guess is printed. 
```
python simulator_solver.py
```
