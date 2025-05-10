# M-E: 3D Maze Escape Game

## Game Overview
Mia and Eva are trapped in a mysterious 3D maze with 9 rooms. Their goal is to find two hidden keys and escape the maze. Players must navigate through the rooms using arrow keys, collecting keys strategically placed in different rooms.

## How to Run the Game
1. Ensure you have Python 3.8+ installed
2. Install dependencies: `pip install -r requirements.txt`
3. Run the game: `python src/maze.py`

## Game Mechanics
- The maze is a 3x3 grid representing 9 interconnected rooms
- Use arrow keys to move:
  - ⬆️ Move Up
  - ⬇️ Move Down
  - ⬅️ Move Left
  - ➡️ Move Right
- Collect 2 keys to win the game
- Keys are randomly placed in different rooms each game

## Functions and Application Structure
### `MazeGame` Class
- `__init__()`: Initializes game window, maze layout, and player
- `_generate_key_locations()`: Randomly places keys in rooms
- `move_player()`: Handles player movement within maze boundaries
- `_check_key_collection()`: Checks if player has collected a key
- `is_game_won()`: Determines if all keys are collected
- `render()`: Renders the 3D maze view (placeholder)
- `run()`: Main game loop handling events and game logic

## Future Improvements
- Implement full 3D rendering
- Add more complex maze generation
- Include player and environment textures
