import random
import os

# Game constants
BOARD_SIZE = 10
SHIPS = [
    ("Carrier", 5),
    ("Battleship", 4),
    ("Cruiser", 3),
    ("Submarine", 3),
    ("Destroyer", 2)
]

# Board symbols
WATER = '~'
HIT = 'X'
MISS = 'O'
SHIP = 'S'

def create_board():
    """Create an empty board filled with water."""
    pass

def display_board(board):
    """Display the board with coordinates (1-indexed)"""
    # board is 0-indexed. 
    # Create column headers with proper alignment
    
    # Print column headers
    
    # Iterate over the board. If cell is a ship, display a water cell, otherwise display the cell. In each inner loop, remember to print the row number in the leftmost column.
    for i in range(BOARD_SIZE):
        pass

def is_valid_position(board, row, col, length, direction):
    """Check if ship placement is valid."""
    # For each direction, check if the ship can be placed on the board. If it can, make sure the ship does not overlap with any other ship. If it does, return False. If it doesn't, return True.
    if direction == 'horizontal':
        pass
    else:  # vertical
        pass
    return True

def place_ship(board, row, col, length, direction):
    """Place a ship on the board."""
    if direction == 'horizontal':
        for c in range(col, col + length):
            board[row][c] = SHIP
    else:  # vertical
        for r in range(row, row + length):
            board[r][col] = SHIP

def place_ships_randomly(board, ships):
    """Randomly place all ships on the board."""
    # For each ship, try to place it on the board. If it can't be placed, try again. Use randomness to choose the direction and the position. Use the is_valid_position function to check if the ship can be placed. Use the place_ship function to place the ship on the board.
    for ship_name, ship_length in ships:
        placed = False
        attempts = 0
        max_attempts = 100
        
        while not placed and attempts < max_attempts:
            pass
        

def get_player_guess():
    """Get coordinates from player input. Users will give us coordinates in 1 indexed format (like 3 5). We need to convert them to 0 indexed format (like 2 4)."""
    # Takes the users input and validates if only 2 numbers are entered, if they are between 1 to 10, and they are valid numbers (not letters or special characters)

    while True:
        try:
            pass
        except ValueError:
            print("Please enter valid numbers.")

def make_guess(board, row, col):
    """Make a guess and update the board. Return the result."""
    # Update the board with the guess, if it is a hit, return "hit", if it is a miss, return "miss", if it is already guessed, return "already_guessed"
    pass

def count_remaining_ships(board):
    """Count how many unhit ship parts are left."""
    # Count the number of SHIP cells on the board
    count = 0
    pass
    return count

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_game_stats(turns, hits, misses):
    """Display current game statistics."""
    print(f"\n--- Game Stats ---")
    print(f"Turns: {turns}")
    print(f"Hits: {hits}")
    print(f"Misses: {misses}")
    if turns > 0:
        accuracy = (hits / turns) * 100
        print(f"Accuracy: {accuracy:.1f}%")

def play_battleships():
    """Main game function."""
    print("=" * 50)
    print("    WELCOME TO BATTLESHIPS! (Single Board)")
    print("=" * 50)
    print("\nRules:")
    print("- Find and sink all enemy ships")
    print("- Enter coordinates as 'row col' (e.g., '3 5')")
    print("- Coordinates range from 1 to 10")
    print("- 'X' = Hit, 'O' = Miss, '~' = Water")
    print(f"- Board size: {BOARD_SIZE}x{BOARD_SIZE}")
    print("- Ships to find:")
    for ship_name, ship_length in SHIPS:
        print(f"  • {ship_name} (length {ship_length})")
    
    input("\nPress Enter to start the game...")
    
    # Initialize game with single board
    board = create_board()
    
    # Place ships randomly on board
    place_ships_randomly(board, SHIPS)
    
    # Game statistics
    turns = 0
    hits = 0
    misses = 0
    total_ship_parts = sum(ship[1] for ship in SHIPS)
    
    print(f"\nAll ships have been placed! You need to sink {total_ship_parts} ship parts.")
    
    # Main game loop
    while True:
        clear_screen()
        print("=" * 50)
        print("    BATTLESHIPS - Your Guesses (Single Board)")
        print("=" * 50)
        
        # Display the board (hiding unhit ships)
        display_board(board)
        display_game_stats(turns, hits, misses)
        
        remaining_ships = count_remaining_ships(board)
        print(f"\nShip parts remaining: {remaining_ships}")
        
        # Check win condition
        if remaining_ships == 0:
            print("\n" + "=" * 50)
            print("🎉 CONGRATULATIONS! YOU WON! 🎉")
            print("=" * 50)
            print(f"You sank all ships in {turns} turns!")
            display_game_stats(turns, hits, misses)
            break
        
        # Get player guess
        row, col = get_player_guess()
        
        # Make the guess
        result = make_guess(board, row, col)
        turns += 1
        
        if result == "already_guessed":
            print("You already guessed that position! Try again.")
            turns -= 1  # Don't count repeated guesses
            input("Press Enter to continue...")
            continue
        elif result == "hit":
            print("🎯 HIT! Great shot!")
            hits += 1
        elif result == "miss":
            print("💦 Miss! Try again.")
            misses += 1
        
        input("Press Enter to continue...")
    
    # Show final board with all ships revealed
    print("\nFinal board with all ships revealed:")
    display_board(board)
    
    # Ask if player wants to play again. If they say yes, play the game again. If they say no, print a goodbye message and exit the game. If they say anything else, just ask again.
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
        pass

if __name__ == "__main__":
    play_battleships()
