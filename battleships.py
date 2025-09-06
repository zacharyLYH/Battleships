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
    return [[WATER for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def display_board(board):
    """Display the board with coordinates (1-indexed). Hide ships if hide_ships=True."""
    # Create column headers with proper alignment
    col_headers = []
    for i in range(1, BOARD_SIZE + 1):
        if i == 10:
            col_headers.append(str(i))
        else:
            col_headers.append(f" {i}")
    
    print("\n     " + " ".join(col_headers))
    print("   " + "-" * (len(" ".join(col_headers)) + 1))
    
    for i in range(BOARD_SIZE):
        row_display = []
        for j in range(BOARD_SIZE):
            cell = board[i][j]
            # Hide unhit ships from player view
            if cell == SHIP:
                row_display.append(WATER)
            else:
                row_display.append(cell)
        # Row numbers are 1-indexed, right-aligned to 2 characters
        print(f"{i+1:2} | " + " ".join(f" {cell}" for cell in row_display))

def is_valid_position(board, row, col, length, direction):
    """Check if ship placement is valid."""
    if direction == 'horizontal':
        if col + length > BOARD_SIZE:
            return False
        for c in range(col, col + length):
            if board[row][c] != WATER:
                return False
    else:  # vertical
        if row + length > BOARD_SIZE:
            return False
        for r in range(row, row + length):
            if board[r][col] != WATER:
                return False
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
    for ship_name, ship_length in ships:
        placed = False
        attempts = 0
        max_attempts = 100
        
        while not placed and attempts < max_attempts:
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            direction = random.choice(['horizontal', 'vertical'])
            
            if is_valid_position(board, row, col, ship_length, direction):
                place_ship(board, row, col, ship_length, direction)
                placed = True
            
            attempts += 1
        
        if not placed:
            print(f"Warning: Could not place {ship_name}")

def get_player_guess():
    """Get coordinates from player input (1-indexed, converted to 0-indexed internally)."""
    while True:
        try:
            guess = input("\nEnter your guess (row col), e.g., '3 5': ").strip().split()
            if len(guess) != 2:
                print("Please enter exactly two numbers separated by a space.")
                continue
            
            row, col = int(guess[0]), int(guess[1])
            
            # Convert from 1-indexed to 0-indexed
            row -= 1
            col -= 1
            
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                return row, col
            else:
                print(f"Coordinates must be between 1 and {BOARD_SIZE}.")
        except ValueError:
            print("Please enter valid numbers.")

def make_guess(board, row, col):
    """Make a guess and update the board. Return the result."""
    cell = board[row][col]
    
    # Check if already guessed
    if cell == HIT or cell == MISS:
        return "already_guessed"
    
    # Check if it's a ship
    if cell == SHIP:
        board[row][col] = HIT
        return "hit"
    else:
        board[row][col] = MISS
        return "miss"

def count_remaining_ships(board):
    """Count how many unhit ship parts are left."""
    count = 0
    for row in board:
        for cell in row:
            if cell == SHIP:  # Only count unhit ships
                count += 1
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
    
    # Ask if player wants to play again
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
        if play_again in ['y', 'yes']:
            play_battleships()
            return
        elif play_again in ['n', 'no']:
            print("Thanks for playing Battleships! Goodbye! 👋")
            return
        else:
            print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    play_battleships()
