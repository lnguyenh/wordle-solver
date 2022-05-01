# Wordle Solver

## About
Our family discovered the New-York-Times Wordle game a few weeks ago, and since then it has been a fun daily activity that we share with our kids.

The game can be found here https://www.nytimes.com/games/wordle/index.html.

It started to itch me to make a program able to solve the daily puzzles and this repo is a playground for this.

## Quickstart

### Setup
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

### Run The Fully Automatic Solve 
This uses Selenium to open the Wordle website in a browser and solve the puzzle of the day without any user input.
```
python -m solvers.browser_solver
```

### Run The Assistant Solver
This is a CLI tool where you tell the program about new constraints, and it will suggest a few words for the next guess.
```
python -m solvers.cli_assistant_solver
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
This is a CLI Wordle simulation. The user chooses a solution word and lets the program find it. Each guess along the way is printed. 
```
python -m solvers.simulator_solver
```
