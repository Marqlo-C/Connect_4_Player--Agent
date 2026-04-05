# Connect 4 Player Agents

This repository contains a Connect 4 game engine plus multiple player agents, including:
- Human players (GUI and console)
- Baseline AIs (random and heuristic)
- Monte Carlo simulation AI
- Minimax AI
- Alpha-Beta pruning AI

The project can be used to:
- Play Connect 4 with a GUI or in console mode
- Run AI vs AI matches
- Benchmark agent performance using the included test scripts

## Project Files

- game_launcher.py: CLI entry point to run a game with configurable players and options.
- connect4.py: Core game engine, board state, move execution, win/tie detection, visualization support, and optional per-turn time limits.
- marqlo_players_final_ver.py: Primary player implementations used by game_launcher.py and test scripts.
- montecarlo.py: Monte Carlo agent implementation used by game_launcher.py.
- thread.py: Killable thread utility used for move time limiting.
- matchup_visualizer.py: Matchup visualization/evaluation script (alpha-beta vs selected competitors).
- eval_diagnostics.py: Evaluation-function diagnostic script for alpha-beta scoring.

## Requirements

Python 3.9+ is recommended.

Install dependencies:

```bash
python -m pip install numpy pygame
```

## Quick Start

Run a local game:

```bash
python game_launcher.py
```

Using the project virtual environment:

```bash
source .venv/bin/activate
python game_launcher.py
```

Defaults are:
- Player 1: humanGUI
- Player 2: humanGUI
- Board: 6 rows x 7 columns

Run AI vs AI (no GUI):

```bash
python game_launcher.py -p1 alphaBetaAI -p2 monteCarloAI -visualize False -verbose False
```

Run console human vs AI:

```bash
python game_launcher.py -p1 humanConsole -p2 alphaBetaAI -visualize False -verbose True
```

## CLI Options

The main script supports the following arguments:

- -w: Number of rows (default: 6)
- -l: Number of columns (default: 7)
- -p1: Player 1 agent class name
- -p2: Player 2 agent class name
- -seed: Random seed (default: 0)
- -visualize: True or False (string)
- -verbose: True or False (string)
- -limit_players: Comma-separated player numbers to time-limit (default: 1,2)
- -time_limit: Comma-separated per-player limits in seconds (default: 1.0,1.0)
- -cvd_mode: True or False (string), toggles colorblind-friendly palette
- -print_time_logs: True or False (string), intended to print per-turn timing details

Available agents in game_launcher.py:
- humanGUI
- humanConsole
- stupidAI
- randomAI
- monteCarloAI
- minimaxAI
- alphaBetaAI

## How The Time Limit Works

The engine can time-limit selected players per move.

- If a player's move exceeds its configured limit, the move thread is terminated.
- The engine then substitutes a legal random move.

This mechanism is implemented in connect4.py using thread_with_trace from thread.py.

## Testing / Evaluation

### 1) Matchup benchmark

Run:

```bash
python matchup_visualizer.py
```

What it does:
- Plays alphaBetaAI from marqlo_players_final_ver.py against randomAI and monteCarloAI.
- Runs both starting positions (you first / you second).
- Reports wins, ties, losses, and total points.

### 2) Evaluation function debugging

Run:

```bash
python eval_diagnostics.py
```

What it does:
- Builds a mock board state.
- Prints scoring contributions (horizontal, vertical, diagonal, center control).
- Helps inspect alpha-beta heuristic behavior.

## Implementing Your Own Agent

To add a new player agent:

1. Inherit from connect4Player.
2. Implement play(self, env, move_dict).
3. Write your chosen column to move_dict['move'].
4. Register your class in the agents mapping in game_launcher.py.

Notes:
- env is a deep-copied game state, so you can simulate safely.
- Legal moves are columns where env.topPosition[col] >= 0.

## Known Behavior Notes

- The boolean-style CLI flags are parsed as strings and must be passed as True or False.
- The print_time_logs flag is passed through as a string in game_launcher.py; in Python, non-empty strings evaluate as truthy.
- GUI drawing constants are fixed to the standard 6x7 layout dimensions.

## License / Attribution

The visualization path in connect4.py references Connect 4 pygame code used with permission from Keith Galli:
https://github.com/KeithGalli/Connect4-Python
